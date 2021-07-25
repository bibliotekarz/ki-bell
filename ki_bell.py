import socket
import machine


def read_sensor() -> list:
    try:
        pr = machine.ADC(0)
        swieci = pr.read()

        data = ["https://raw.githubusercontent.com/bibliotekarz/ki-bell/master/img/wolne.jpg", "wolne", "green",
                "lightgreen", "0f0"]

        print("wartość swieci ", swieci)
        if swieci > 250:
            data = ["https://raw.githubusercontent.com/bibliotekarz/ki-bell/master/img/zajete.jpg", "zajęte",
                    "red", "lightcoral", "f00"]

    except OSError as e:
        return ('Failed to read sensor.')

    return data


def web_page(czy_swieci: list) -> str:
    html = """<!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
        <meta charset="UTF-8">
        <title>Projekt Ki-Bell</title>
        <link rel="icon" href="data:image/svg+xml,%3Csvg%20viewBox='0%200%2046%2045'%20xmlns='http://www.w3.org/2000/svg'%3E%3Ctitle%3EAfter%20Dark%3C/title%3E%3Cpath%20d='M.708%2045L23%20.416%2045.292%2045H.708zM35%2038L23%2019%2011%2038h24z'%20fill='%23""" + \
           czy_swieci[
               4] + """'/%3E%3C/svg%3E" type="image/x-icon"/ > </head> <body> <div style='text-transform: uppercase; text-align: center; color: """ + \
           czy_swieci[2] + """; border: double; background-color: """ + czy_swieci[3] + """;'> 
        
        <h1>WC jest """ + czy_swieci[1] + """.</h1>
        <img src='""" + czy_swieci[0] + """' alt='stan ubikacji - """ + czy_swieci[1] + """'>
        <br /><br />
        </div>
    </body>
    </html>\r\n"""

    return html


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(4)

while True:
    cl, addr = s.accept()
    result = read_sensor()
    response = web_page(result)
    cl.recv(2048)
    cl.send('HTTP/1.1 200 OK\r\n')
    cl.send('Content-Type: text/html; charset=UTF-8\r\n\r\n')
    cl.sendall(response.encode('utf-8'))
    cl.close()

    print('Got a connection from %s' % str(addr))
