#Exercise 3
#Read sensor dara, transmit via wifi and bluetooth
#print results and define ranges

import pycom
import machine
import time
from network import Bluetooth

pycom.heartbeat(False)

#connect to bluetooth
#bluetooth = Bluetooth()
#bluetooth.connect("Alejandra's iPhone")

#Read sensor data
#adc = machine.ADC()
#apin = adc.channel(pin='P16') #read pin 16- where the sensor would be
sensor_data = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
i = 0

while True:
  #val = apin.voltage() # read data
  val = sensor_data[i]
  i = i + 1
  if i > 10:
      i = 0
  print(val) #print on screen

  #Trasmit data
  pybytes.send_signal(2,val)

  #Classify data
  if val <= 10:
      pycom.rgbled(0xfdfefe) #white
  elif val > 10 and val <= 20:
      pycom.rgbled(0x0000ff) #blue
  elif val > 20 and val <= 30:
      pycom.rgbled(0x00ff00) #Green
  elif val > 30 and val <= 40:
      pycom.rgbled(0xfefa00) #yellow
  elif val > 40:
      pycom.rgbled(0xf39c12) #orange
  else:
      pycom.rgbled(0xff0000) #Red
      #data out of range

  time.sleep(2)
