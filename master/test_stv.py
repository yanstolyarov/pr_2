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
import serial1 as S

#MD.motor_pwm_forw_1(x)
#MD.motor_pwm_forw_2(x)
#MD.motor_pwm_reverse_1(x)
#MD.motor_pwm_reverse_2(x)
#MD.all_motor_pwm_forward(x)
#MD.all_motor_pwm_reverse(x)
#MD.stop()
#1 - left, 2 - right, x - power(0-100)

#side = right
t_a = 0.2 #time of moving forward/backward to make 1 step
t_b = 0.5 #time for turn on 90 degrees
t_c = 0.2 #time for come in turn
t_d = 2.2 #time for come out of turn
p_s = 30 #power for steps
p_t = 35 #power for turns
c_a = 31 #dalnomer critical value

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
    but_f = button1_status()
    dm_2 = S.dm_2()
    print('button: ',but_f, 'distance: ', dm_2)
    #print 'Operation: ', counter
    #counter = counter + 1
    # any algorithm code
    # can be put here

    # check for buttons pressed
    #key = anykey()
    #if key == chr(119):
    #    print 'forward'
    #if key == chr(115):
    #    print ('reverse')
    #if key == chr(100):
    #    print ('right')
    #if key == chr(97):
    #    print ('left')
    #if key == chr(32):
    #    print ('stop')
    if but_f == 0 and dm_2 <= c_a:
        MD.stop()
        but_f = button1_status()
        dm_2 = S.dm_2()
        print('button: ',but_f, 'distance: ', dm_2)
        time.sleep(0.1)

        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_a)
        MD.stop()
        but_f = button1_status()
        time.sleep(0.1)

    if but_f == 0 and dm_2 > c_a:
        MD.stop()
        but_f = button1_status()
        dm_2 = S.dm_2()
        print('button: ',but_f, 'distance: ', dm_2)
        time.sleep(0.1)
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_c)
        MD.stop()
        MD.motor_pwm_forw_2(p_t)
        MD.motor_pwm_reverse_1(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_d)
        MD.stop()
        but_f = button1_status()
        time.sleep(0.1)

    if but_f == 1 and dm_2 <= c_a:
        MD.stop()
        but_f = button1_status()
        dm_2 = S.dm_2()
        print('button: ',but_f, 'distance: ', dm_2)
        time.sleep(0.1)
        MD.all_motor_pwm_reverse(p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_pwm_forw_1(p_t)
        MD.motor_pwm_reverse_2(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_c)
        MD.stop()
        time.sleep(0.1)

#    if but_f == 1 and dm_2 > c_a:
 #       MD.stop()
  #      but_f = button1_status()
  #      dm_2 = S.dm_2()
  #      print('button: ',but_f, 'distance: ', dm_2)
 #       time.sleep(0.5)#
#
  #      MD.all_motor_pwm_reverse(p_s)
   #     time.sleep(t_a)
    #    MD.stop()
     #   MD.motor_pwm_forw_2(p_t)
     #   MD.motor_pwm_reverse_1(p_t)
     #   time.sleep(t_b)
     #   MD.stop()
     ##   MD.all_motor_pwm_forward(p_s)
     #   time.sleep(t_d)
     #   MD.stop()
     #   but_f = button1_status()
     #   dm_2 = S.dm_2()
     #   print('button: ',but_f, 'distance: ', dm_2)
     #   time.sleep(0.5)

    #time.sleep(0.1)
