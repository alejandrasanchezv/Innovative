#Exercise 3
#Read sensor dara, transmit via wifi and bluetooth
#print results and define ranges

import pycom
import machine
import time
from network import Bluetooth

pycom.heartbeat(False)

#connect to bluetooth
bluetooth = Bluetooth()

def conn_bt (bt):
    events = bt.events()
    if events and Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events and Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")

def char_handler(chr, data):
    events, value = data
    if events and Bluetooth.CHAR_WRITE_EVENT:
        print("Write request with value = {}".format(value))
    else:
        print("Read request on char 1")

def conectandobt():
    bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
    bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
    bluetooth.advertise(True)

    bluetooth.start_scan(-1)
    adv = None
    #t = 0
    #i = 0
    while True:
        adv = bluetooth.get_adv()
        if adv:
            try:
                bluetooth.connect(adv.mac)
            except:
                # start scanning again
                bluetooth.start_scan(-1)
                continue
            break


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
    print(val)

    conectandobt()
    sensor_bt = bluetooth.service(uuid=b'1108982705950701', isprimary=True)
    sensor_chr = sensor_bt.characteristic(uuid=b'1108982705950702', value=val)
    char_sens = sensor_chr.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char_handler(sensor_chr,5))

    time.sleep(3)
