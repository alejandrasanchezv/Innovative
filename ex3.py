#Exercise 3
#Read sensor dara, transmit via wifi and bluetooth
#print results and define ranges

import pycom
import machine
import time
from network import Bluetooth

update = False
temp = 0

def conn_bt (bt):
    events = bt.events()
    if events and Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events and Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")
        update = False

def char_handler(chr):
    global temp
    global update
    events = chr.events()
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(temp)
        print("transmitted:",temp)
        if events and Bluetooth.CHAR_WRITE_EVENT:
            update = True

def update_handler():
    global temp
    global update
    if update:
        sensor_chr.value(str(temp))

pycom.heartbeat(False)

#connect to bluetooth
bluetooth = Bluetooth()
bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
bluetooth.advertise(True)
sensor_srv = bluetooth.service(uuid=b'1108982705950701', isprimary=True)
sensor_chr = sensor_srv.characteristic(uuid=b'1108982705950702', value= b'0x45')
sensor_chr.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char_handler)
print('Start BLE service')

sensordata = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
i = 0

while True:
    #val = apin.voltage() # read data
    temp = sensordata[i]

    i = i + 1
    if i > 10:
      i = 0

    #Trasmit data
    pybytes.send_signal(2,temp)
    update_handler()
    print(temp)

    #Classify data
    if temp <= 10:
      pycom.rgbled(0xfdfefe) #white
    elif temp > 10 and temp <= 20:
      pycom.rgbled(0x0000ff) #blue
    elif temp > 20 and temp <= 30:
      pycom.rgbled(0x00ff00) #Green
    elif temp > 30 and temp <= 40:
      pycom.rgbled(0xfefa00) #yellow
    elif temp > 40:
      pycom.rgbled(0xf39c12) #orange
    else:
      pycom.rgbled(0xff0000) #Red
      #data out of range

    time.sleep(5)
