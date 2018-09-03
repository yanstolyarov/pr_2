#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import motor_driver_new as MD
import com_distance_sensor1 as DS1
import time
from RPi import GPIO
#initialise a previous input variable to 0 (assume button not pressed last)
#prev_input = 0

#adjust for where your switch is connected
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

but_1 = button1_status()

while True:
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
         MD.motor_pwm_forw_1(p8)
         MD.motor_pwm_forw_2(p7) 
         time.sleep(1)
         MD.stop() 
         dm_1 = DS1.dm_1()
             if DS1.dm_1() < l:
                 MD.motor_pwm_forw_1(p6)
                 MD.motor_pwm_forw_2(p5) 
                 time.sleep(1)
                 MD.stop()       
     else:
         MD.motor_pwm_forw_1(p4)
         MD.motor_pwm_forw_2(p3)
         time.sleep(1)
         MD.stop()
         dm_1 = DS1.dm_1()
         if DS1.dm_1() < l:
             MD.motor_pwm_forw_1(p6)
             MD.motor_pwm_forw_2(p5) 
             time.sleep(1)
             MD.stop() 
   
