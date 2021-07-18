import socket
import time


# import machine


def read_sensor()->list:
    try:
        #        pr = machine.ADC(0)
        #        swieci = pr.read()

        data = ["https://raw.githubusercontent.com/bibliotekarz/ki-bell/master/img/wolne.jpg", "wolne", "green",
                "lightgreen", "0f0"]
        swieci = 200  # zaślepka testowa
        print("wartość swieci ", swieci)
        if swieci > 250:
            data = ["https://raw.githubusercontent.com/bibliotekarz/ki-bell/master/img/zajete.jpg", "zajęte",
                    "red", "lightcoral", "f00"]

    except OSError as e:
        return ('Failed to read sensor.')

    return data


def web_page(czy_swieci:list)->str:
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="5">
    <meta charset="UTF-8">
    <title>Projekt Ki-Bell</title>
    <link rel="icon" href="data:image/svg+xml,<svg viewBox='0 0 46 45' xmlns='http://www.w3.org/2000/svg'><title>Status</title><path d='M.708 45L23 .416 45.292 45H.708zM35 38L23 19 11 38h24z'  fill='#{czy_swieci[4]}'/></svg>" type="image/x-icon"/ > </head> <body> <div style='text-transform: uppercase; text-align: center; color: {czy_swieci[2]}; border: double; background-color: {czy_swieci[3]};'> 
    <h1>WC jest {czy_swieci[1]}.</h1>
    <img src='{czy_swieci[0]}' alt='stan ubikacji - {czy_swieci[1]}'>
    <br /><br />
    </div>
</body>
</html>"""
    return html


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    cl, addr = s.accept()
    result = read_sensor()
    response = web_page(result)
    cl.sendall(response.encode('utf-8'))
    time.sleep(5)
    cl.close()
