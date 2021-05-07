from network import Sigfox
import socket
import pycom
import time


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


# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)


# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)

# send some bytes
s.send(bytes([1, 2, 3]))

# await DOWNLINK message
r = s.recv(32)
print(ubinascii.hexlify(r))

frec = sigfox.frequencies()
print('Uplink frequency:',frec[0])
print('Downlink frequency:',frec[1])
rssi_sigfox = sigfox.rssi()
print(rssi_sigfox)
signalclassf(rssi_sigfox)
