#!/usr/bin/env python
import time
import serial

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/ttyUSB0'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

while 1:
    x = ser.read(17)
    x = x.replace(' ','0')
    x1 = x[3:6]
    x2 = x[8:11]
    x3 = x[13:18]
    print('---------------')
    print(x)
    millis = int(round(time.time() * 1000))
    print('time', millis)
    print(int(x1))
    print(int(x2))
    print(int(x3))
    time.sleep(0.1)
