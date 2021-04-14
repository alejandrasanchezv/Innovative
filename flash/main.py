#LESS ANNOYING RELEASE

from network import WLAN
import pycom
import time

pycom.heartbeat(False) #activate LED

pycom.rgbled(0xf1447c) #Pink
time.sleep(2) 
pycom.rgbled(0xf39c12) #Red
time.sleep(2)

pycom.heartbeat(True) #de-activate LED
