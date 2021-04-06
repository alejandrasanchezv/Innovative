#Exercise 2
#Connect the fipy via wifi and
#use led to inform results

from network import WLAN
import machine
import pycom

pycom.heartbeat(False) #activate LED

wlan = WLAN()
wlan.init(ssid="Home&Life SuperWiFi-D7A1", auth=(WLAN.WPA2, "PLD74M8HH8AGGYFB"))
#connect to wifi

while not wlan.isconnected():
    print("Unable to connect")
    pycom.rgbled(0xff0000) #Red
    machine.idle() #rest

pycom.rgbled(0x00ff00) #Green
