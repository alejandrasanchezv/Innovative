
from network import Sigfox
import binascii

# initalise Sigfox for RCZ1 (You may need a different RCZ Region)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# print Sigfox Device ID
print(binascii.hexlify(sigfox.id()))

# print Sigfox PAC number
print(binascii.hexlify(sigfox.pac()))
