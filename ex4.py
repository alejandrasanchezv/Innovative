import pycom
import machine
import time
from network import WLAN
from network import Bluetooth
import ubinascii

pycom.heartbeat(False)
#pycom.rgbled(0xf1447c) #pink

def conn_bt (bt):
    global info
    events = bt.events()
    if events and Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
        info = bluetooth.get_advertisements()
    elif events and Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")

def scaneando():
    print("Scanning for bluetooth networks")
    bluetooth.start_scan(3)
    while bluetooth.isscanning():
        adv = bluetooth.get_adv()
        if adv:
            # try to get the complete name
            if bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL):
                print('Available networks:', bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))
    time.sleep(2)

def bluetoothlink():
    print('--------- BLUETOOTH ---------')
    bluetooth = Bluetooth()
    scaneando()
    bluetooth.set_advertisement(name='PepeBot', service_uuid=b'1108982705950701')
    bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_bt)
    bluetooth.advertise(True)

    rssi = info[0][3]
    print('Bluetooth link info:', info)
    rssibt = (rssi*-50)/255
    print('Signal level:',rssi)
    return rssibt

def wifilink():
    print('----------- WIFI -----------')
    wlan = WLAN()
    wlan.mode(WLAN.STA)
    original_ssid = wlan.ssid()
    original_auth = wlan.auth()

    print("Scanning for wifi networks")
    available_nets = wlan.scan()
    nets = frozenset([e.ssid for e in available_nets])
    print('Available networks:', nets)

    info = wlan.joined_ap_info()
    print('Wifi link info:', info)
    rssi = info[3]
    print('Signal level:', rssi)
    return rssi

def signalclass(rssi):
    if rssi >= -55:
        pycom.rgbled(0x0000ff) #blue
    elif rssi < -55 and rssi >= -65:
        pycom.rgbled(0x00ff00) #Green
    elif rssi < -65 and rssi >= -75:
        pycom.rgbled(0xffff00) #yellow
    elif rssi < -75 and rssi >= -85:
        pycom.rgbled(0xff8c00) #orange
    else:
        pycom.rgbled(0xff0000) #Red
    time.sleep(5)

rssi_wifi = wifilink()
signalclass(rssi_wifi)

rssi_bt = bluetoothlink()
signalclass(rssi_bt)
