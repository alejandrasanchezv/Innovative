from network import WLAN
import machine
import time

pycom.heartbeat(False)
#pycom.rgbled(0xf1447c) #pink

def wifilink():
    print('----------- WIFI -----------')
    wlan = WLAN()
    wlan.mode(WLAN.STA)
    original_ssid = wlan.ssid()
    original_auth = wlan.auth()

    print("Scanning for known wifi nets")
    available_nets = wlan.scan()
    nets = frozenset([e.ssid for e in available_nets])
    print('Available networks:', nets)

    info = wlan.joined_ap_info()
    print('Wifi link info:', info)
    rssi = info[3]
    print('Signal level:', rssi)
    return rssi

def bluetoothlink():
    print('-------- BLUETOOTH --------')
    bluetooth.get_adv()

def signalclass(rssi):
    if rssi >= -45:
        pycom.rgbled(0x800080) #purple
    elif rssi < -45 and rssi >= -55:
        pycom.rgbled(0x0000ff) #blue
    elif rssi < -55 and rssi >= -65:
        pycom.rgbled(0x00ff00) #Green
    elif rssi < -65 and rssi >= -75:
        pycom.rgbled(0xffff00) #yellow
    elif rssi < -75 and rssi >= -85:
        pycom.rgbled(0xff8c00) #orange
    elif rssi == 0:
        pycom.rgbled(0xffffff) #white
    else:
        pycom.rgbled(0xff0000) #Red

rssi = wifilink()
signalclass(rssi)
