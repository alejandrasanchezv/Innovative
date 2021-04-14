from network import Bluetooth
import ubinascii
import time
#from ble_advertising import advertising_payload

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='FiPy', service_uuid=b'1234567890123456')

def conn_cb (bt_o):
    events = bt_o.events()   # this method returns the flags and clears the internal registry
    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

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

print(".")
#sensor_bt = bluetooth.service(uuid=b'12345678901234766', isprimary=True, nbr_chars=1)
#sensor_chr = sensor_bt.characteristic(uuid=0x00012A59, value=1)
