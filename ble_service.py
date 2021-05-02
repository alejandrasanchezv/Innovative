from network import Bluetooth
import time
from machine import Timer
bluetooth = Bluetooth()

update = False
temp = 0

def conn_bt (bt):
    events = bt.events()
    if events and Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events and Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")
        update = False

def char_handler(chr, data):
    global temp
    global update
    #events, value = data
    events = chr.events()
    #if events and Bluetooth.CHAR_WRITE_EVENT:
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(temp)
        print("transmitted:",temp)
        if events and Bluetooth.CHAR_WRITE_EVENT:
            update = True
        #print("Write request with value = {}".format(value))
    #else:
        #print("Read request on char 1")

# def conectandobt():
#     bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
#     bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
#     bluetooth.advertise(True)

    # bluetooth.start_scan(-1)
    # adv = None
    # while True:
    #     adv = bluetooth.get_adv()
    #     if adv:
    #         try:
    #             bluetooth.connect(adv.mac)
    #         except:
    #             # start scanning again
    #             bluetooth.start_scan(-1)
    #             continue
    #         break

#conectandobt()
bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
bluetooth.advertise(True)
print("hey")
n = str(5)
print(n)
sensor_srv = bluetooth.service(uuid=b'1108982705950701', isprimary=True)
sensor_chr = sensor_srv.characteristic(uuid=b'1108982705950702', value=n)
sensor_chr.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char_handler)
print('Start BLE service')

def update_handler(update_temp):
    global temp
    global update
    #temp  += 5
    if update:
        sensor_chr.value(str(temp))

#update_temp = Timer.Alarm(update_handler, 1, periodic=True)
while True:
    temp  += 5
    #update_temp = Timer.Alarm(update_handler,1, periodic=True)
    #update_handler()
    if update:
        sensor_chr.value(str(temp))
    time.sleep(1)
