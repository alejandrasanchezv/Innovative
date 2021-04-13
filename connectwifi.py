#Exercise 2
#The Fipy connects to the wifi network
#LED: red if it was unable to connect, green connected to wifi
#Doubt: upload the firmware via Wi-Fi

from network import WLAN
import pycom

pycom.heartbeat(False) #activate LED

wlan = WLAN()

while not wlan.isconnected():
    print("Unable to connect")
    pycom.rgbled(0xff0000) #Red
    wlan.init(ssid="Home&Life SuperWiFi-D7A1", auth=(WLAN.WPA2, "PLD74M8HH8AGGYFB"))

pycom.rgbled(0x00ff00) #Green
pybytes.send_signal(1,"Connected")
print("Connected")
