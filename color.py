#Exercise 1
#Turn LED on and switch colors
import pycom
import time

pycom.heartbeat(False)

#pycom.rgbled(0x5cf144) #Green
#time.sleep(5)
#pycom.rgbled(0xff0000) #Red
#time.sleep(5)
#pycom.rgbled(0x0000ff) #Blue
#time.sleep(5)
pycom.rgbled(0xf1447c) #pink
time.sleep(5) # 5 second wait
pycom.rgbled(0xf77207) #orange

pycom.heartbeat(True) #turn led into its initial state
