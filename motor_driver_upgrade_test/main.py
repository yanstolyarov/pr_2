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

#side = right
t_a = 0.9 #time of moving forward/backward to make 1 step
t_b = 0.9 #time for turn on 90 degrees
p_s = 30 #power for steps
p_t = 30 #power for turns
c_a = 10 #dalnomer critical value

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
    key = anykey()
    if key == chr(119):
        print 'forward'
        MD.all_motor_(p_s)
        time.sleep(t_a)
        MD.stop()
    if key == chr(115):
        print ('reverse')
        MD.all_motor_(-p_s)
        time.sleep(t_a)
        MD.stop()
    if key == chr(100):
        print ('right')
        MD.motor_1(p_t)
        MD.motor_2(-p_t)
        time.sleep(t_b)
        MD.stop()
    if key == chr(97):
        print ('left')
        MD.motor_1(-p_t)
        MD.motor_2(p_t)
        time.sleep(t_b)
        MD.stop()

    if key == chr(32):
        print ('stop')
        MD.stop()
        break

#начало алгоритма
    if but_f == 0 and dm_2 <= c_a:
        MD.all_motor_(p_s)
        time.sleep(t_a)
        MD.stop()

    if but_f == 0 and dm_2 > c_a:
        MD.all_motor(p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_1(-p_t)
        MD.motor_2(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor(p_s)
        time.sleep(t_a)
        MD.stop()

    if but_f == 1 and dm_2 <= c_a:
        MD.all_motor(-p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_2(-p_t)
        MD.motor_1(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor(p_s)
        time.sleep(t_a)
        MD.stop()

    if but_f == 1 and dm_2 <= c_a:
        MD.all_motor(-p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_1(-p_t)
        MD.motor_2(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor(p_s)
        time.sleep(t_a)
        MD.stop()
#конец
    time.sleep(0.2)
