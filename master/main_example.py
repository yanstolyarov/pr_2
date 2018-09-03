#!/usr/bin/env python
import os
import time
import select
import sys
import tty
import termios
import atexit
from RPi import GPIO
import motor_driver as MD


GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(10,GPIO.IN)

def button1_status():
    curr1 = GPIO.input(17)
    #print("b1",curr1)
    if curr1 == 0:
        return 1
    else:
        return 0

def button2_status():
    curr2 = GPIO.input(10)
    #print("b2",curr2)
    if curr2 == 0:
        return 1
    else:
        return 0

old_settings = None
def init_anykey():
  global old_settings
  old_settings = termios.tcgetattr(sys.stdin)
  new_settings = termios.tcgetattr(sys.stdin)
  new_settings[3] = new_settings[3] & ~(termios.ECHO | termios.ICANON)
  new_settings[6][termios.VMIN] = 0
  new_settings[6][termios.VTIME] = 0
  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)

@atexit.register
def term_anykey():
  global old_settings
  if old_settings:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def anykey():
  ch_raw = 0
  ch_raw = sys.stdin.read(1)
  return ch_raw

init_anykey()
#counter = 0
while True:
  #print 'Operation: ', counter
  #counter = counter + 1
  # any algorithm code
  # can be put here

  # check for buttons pressed
  #print(button1_status())
  if button1_status() or button2_status():
    print('button pressed')

  key = anykey()
  if key == chr(119):
    print 'forward'
  if key == chr(115):
    print ('reverse')
  if key == chr(100):
    print ('right')
  if key == chr(97):
    print ('left')
  if key == chr(32):
    print ('stop')

  time.sleep(0.2)
