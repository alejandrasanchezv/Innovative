import pycom
import machine
import time
from network import Bluetooth


#rssi = 0

#def seconecto():
    # rssi = 0
    # info = bluetooth.get_advertisements()
    # if Bluetooth.CLIENT_CONNECTED and info:
    #     rssi = info[0]
    #     rssi = rssi[3]
    # return rssi
    # info = bluetooth.get_advertisements()
    # rssi = info[0]
    # rssi = rssi[3]
    # return rssi

def conn_bt (bt):
    events = bt.events()
    if events and Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events and Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")


#connect to bluetooth
bluetooth = Bluetooth()
bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
bluetooth.advertise(True)

if Bluetooth.CLIENT_CONNECTED:
    info = bluetooth.get_advertisements()
    rssi = info[0]
    rssibt = rssi[3]
    print('Rssi =',rssibt)
else:
    print('Disconnected')
#sensor_srv = bluetooth.service(uuid=b'1108982705950701', isprimary=True)
#sensor_chr = sensor_srv.characteristic(uuid=b'1108982705950702', value= b'0x45')


#bluetooth.start_scan(20)






# from network import WLAN
# import machine
#
# print('----------- WIFI -----------')
# wlan = WLAN()
# wlan.mode(WLAN.STA)
# original_ssid = wlan.ssid()
# original_auth = wlan.auth()
#
# print("Scanning for known wifi nets")
# available_nets = wlan.scan()
# nets = frozenset([e.ssid for e in available_nets])
# print('Available networks:', nets)
#
# info = wlan.joined_ap_info()
# print('Wifi link info:', info)
# rssi = info[3]
# print('Signal level:', rssi)

# from network import WLAN
# import ubinascii
#
#
# def pack_cb(pack):
#     mac = bytearray(6)
#     pk = wlan.wifi_packet()
#     control = pk.data[0]
#     subtype = (0xF0 & control) >> 4
#     type = 0x0C & control
#     #print("Control:{}, subtype:{}, type:{}".format(control, subtype, type))
#     if subtype == 4:
#         for i in range (0,6):
#             mac[i] = pk.data[10 + i]
#         print ("Wifi Node with MAC: {}".format(ubinascii.hexlify(mac)))
#
# wlan = WLAN(mode=WLAN.STA, antenna=WLAN.EXT_ANT)
# wlan.callback(trigger=WLAN.EVENT_PKT_MGMT, handler=pack_cb)
# wlan.promiscuous(True)
