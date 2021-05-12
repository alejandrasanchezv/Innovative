import socket
import time
import ubinascii
import pycom
from network import LoRa

pycom.heartbeat(False)

def signalclassf(rssi):
    if rssi >= -122:
        pycom.rgbled(0x00ff00) #Green
    elif rssi < -122 and rssi >= -129:
        pycom.rgbled(0xffff00) #yellow
    elif rssi < -129 and rssi >= -135:
        pycom.rgbled(0xff8c00) #orange
    else:
        pycom.rgbled(0xff0000) #Red

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify('70B3D57ED00425EF')
app_key = ubinascii.unhexlify('2C6DA9613AE3FFE1B518267F75EFEA6D')
dev_eui = ubinascii.unhexlify('70B3D549919F26AA')

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

#IM HAVING TROUBLE WITH THE LORA CONNECTION

print('Joined')
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)


s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))


s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)

frec = lora.frequency()
print('Lora frequency', frec)

stats = lora.stats()
rssi_lora = stats[1]
print(rssi_lora)
signalclassf(rssi_lora)
