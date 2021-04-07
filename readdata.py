#Exercise 3
#Read sensor dara, transmit via wifi and bluetooth
#print results and define ranges

import machine
import time

#Read sensor data
adc = machine.ADC()
apin = adc.channel(pin='P16') #read pin 16- where the sensor would be

while True:
  millivolts = apin.voltage() # read data
  print(millivolts) #print on screen

  #Trasmit data
  

  time.sleep(1)
