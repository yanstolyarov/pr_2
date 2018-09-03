#!/usr/bin/env python
import time
import serial

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/ttyUSB0'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

def dm_1():
    x = ser.read(17)
    x = x.replace(' ','0')
    x1 = x[3:6]
    x1 = int(x1)
    return x1

def dm_2():
    x = ser.read(17)
    x = x.replace(' ','0')
    x2 = x[8:11]
    x2 = int(x2)
    return x2

def dlin():
    x = ser.read(17)
    x = x.replace(' ','0')
    x3 = x[13:18]
    x3 = int(x3)
    return x3
