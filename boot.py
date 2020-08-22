import gc
import time

import network
import webrepl

webrepl.start()
gc.collect()

nazwa_sieci = "wifi"
haslo_sieci = "pass"

network.WLAN(network.AP_IF).active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.config(dhcp_hostname="ki-bell")
sta_if.active(True)
sta_if.connect('nazwa_sieci', 'haslo_sieci')

count = 0
while not sta_if.isconnected():
	time.sleep_ms(1)
	count += 1
	if count==10000:
		print('Not connected')
		break
print('Config: ', sta_if.ifconfig())
