#Sigfox
from network import Sigfox
import socket

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


















#BLUETOOTH

# import pycom
# import machine
# import time
# from network import Bluetooth
# import ubinascii
#
# def conn_bt (bt):
#     global info
#     events = bt.events()
#     if events and Bluetooth.CLIENT_CONNECTED:
#         print("Client connected")
#         info = bluetooth.get_advertisements()
#     elif events and Bluetooth.CLIENT_DISCONNECTED:
#         print("Client disconnected")
#
# def scaneando():
#     bluetooth.start_scan(5)
#     while bluetooth.isscanning():
#         adv = bluetooth.get_adv()
#         if adv:
#             # try to get the complete name
#             if bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL):
#                 print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))
#
#             # mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)
#             #
#             # if mfg_data:
#             #     # try to get the manufacturer data (Apple's iBeacon data is sent here)
#             #     print(ubinascii.hexlify(mfg_data))
#
#     time.sleep(2)
#
# #connect to bluetooth
# bluetooth = Bluetooth()
# scaneando()
# bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
# bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
# bluetooth.advertise(True)
#
# # if Bluetooth.CLIENT_CONNECTED:
# # info = bluetooth.get_advertisements()
# #info = info[0]
# #print(info)
# rssi = info[0][3]
# rssibt = (rssi*-50)/255
# print('Rssi =',rssibt)





#WIFI

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
