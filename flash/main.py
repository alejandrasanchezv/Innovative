#Exercise 2
#The Fipy connects to the wifi network
#LED: red if it was unable to connect, green connected to wifi

from network import WLAN
import pycom

pycom.heartbeat(False) #activate LED

wlan = WLAN()

while not wlan.isconnected():
    pycom.rgbled(0xff0000) #Red
    wlan.init(ssid="FASTWEB-E08271", auth=(WLAN.WPA2, "73FCY921GC"))

pycom.rgbled(0x00ff00) #Green
pybytes.send_signal(1,"Connected")
print("Connected")
