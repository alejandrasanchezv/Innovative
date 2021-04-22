from network import Bluetooth
import time
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

conectandobt()
print("hey")
#i = 15
sensor_bt = bluetooth.service(uuid=b'1108982705950701', isprimary=True)
sensor_chr = sensor_bt.characteristic(uuid=b'1108982705950702', value=1)
char_sens = sensor_chr.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char_handler(sensor_chr,5))
