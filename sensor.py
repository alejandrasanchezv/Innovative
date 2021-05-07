import time
import pycom
from pysense import Pysense
import machine

from SI7006A20 import SI7006A20

pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white
py = Pysense()


si = SI7006A20(py)
print("Temperature: " + str(si.temperature())+ " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
print("Dew point: "+ str(si.dew_point()) + " deg C")
t_ambient = 24.4
print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")
