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
import serial as S

#запрос состояния первого дальномера: S.dm_1()
#запрос состояния второго дальномера: S.dm_2()
#запрос показаний датчика линий: s.dlin()
#управление двигателями
#MD.motor_pwm_forw_1(x)
#MD.motor_pwm_forw_2(x)
#MD.motor_pwm_reverse_1(x)
#MD.motor_pwm_reverse_2(x)
#MD.all_motor_pwm_forward(x)
#MD.all_motor_pwm_reverse(x)
#MD.stop()
#1 - left, 2 - right, x - power(0-100)


GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(10,GPIO.IN)
l = 15
p1= 30 #for both engines to move forward
p2=70  #fot both engines to move back
p3 = 90 # for right engine to turn +90
p4=50 #on the left engine to turn +90
p5=90 #on the right engine to turn -90
p6=50 #on the left engine to turn -90
p7=70 #on the right engine for turn +180
p8=20 #on the left engine for turn +180
button_delay = 0.3

sleep = 0.1
power = 40
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
    MD.all_motor_pwm_forward(p1)
    time.sleep(1)
    MD.stop()
    but_1 = button1_status()
    dm_1 = DS1.dm_1()
    if but_1 ==1:
        MD.all_motor_pwm_reverse(p2)
        MD.motor_pwm_forw_1(p4)
        MD.motor_pwm_forw_2(p3)
        time.sleep(1)
        MD.stop()
        dm_1 = DS1.dm_1()
        if DS1.dm_1() < l:        
        MD.motor_pwm_rerverse_1(p8)
        MD.motor_pwm_forw_2(p7) 
        time.sleep(1)
        MD.stop() 
        dm_1 = DS1.dm_1()
            if DS1.dm_1() < l:
                MD.motor_pwm_forw_1(p6)
                MD.motor_pwm_reverse_2(p5) 
                time.sleep(1)
                MD.stop()       
    else:
        MD.motor_pwm_reverse_1(p4)
        MD.motor_pwm_forw_2(p3)
        time.sleep(1)
        MD.stop()
        dm_1 = DS1.dm_1()
        if DS1.dm_1() < l:
            MD.motor_pwm_forw_1(p6)
            MD.motor_pwm_reverse_2(p5) 
            time.sleep(1)
            MD.stop() 
  # check for buttons pressed
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
