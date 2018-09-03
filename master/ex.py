#!/usr/bin/env python
import time
from RPi import GPIO
import motor_driver as MD
import serial1 as S

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

power1 = 20
power_step = 30
power_turn = 20
t_a = 1
time_turn = 1.4
time_in_turn = 1.2
time_out_of_turn = 1.2
time_reverse = 1
dm_crit = 25

while True:
    but_1 = button1_status()
    but_2 = button2_status()
    dm = S.dm_2()
    print('button1: ',but_1,'button2:', but_2, 'distance: ', dm)

    if (but_1 == 0 and but_2 == 0) and dm <= dm_crit:
        for a in range(1,10):#wall alignment via distance sensor
            dm = S.dm_2()
            MD.motor_1(+power1)#small right turn
            MD.motor_2(-power1)#small right turn
            time.sleep(0.3/a)
            MD.stop()
            if S.dm_2() > dm:
                MD.motor_1(-power1)#small left turn
                MD.motor_2(+power1)#small left turn
                time.sleep(0.3/a)
                MD.stop()
        #move forward
        if dm > 9:
            MD.motor_1(power_step)
            MD.motor_2(power_step + 4)
            time.sleep(t_a)
        if dm < 9:
            MD.motor_1(power_step + 4)
            MD.motor_2(power_step)
            time.sleep(t_a)
        else:
            MD.motor_1(power_step)
            MD.motor_2(power_step)
            time.sleep(t_a)
        MD.stop()

        but_1 = button1_status()
        but_2 = button2_status()
        dm = S.dm_2()
        print('button1: ',but_1,'button2:', but_2, 'distance: ', dm)

    if (but_1 == 0 and but_2 == 0) and dm > dm_crit:
        #turn left
        MD.motor_1(power_step)
        MD.motor_2(power_step)
        time.sleep(time_in_turn)
        MD.stop()
        MD.motor_1(-power_turn)
        MD.motor_2(power_turn)
        time.sleep(time_turn)
        MD.stop()
        MD.motor_1(power_step)
        MD.motor_2(power_step)
        time.sleep(time_out_of_turn)
        MD.stop()
        but_1 = button1_status()
        but_2 = button2_status()
        dm = S.dm_2()
        print('button1: ',but_1,'button2:', but_2, 'distance: ', dm)


    if (but_1 == 1 or but_2 == 1) and dm <= dm_crit:
        #turn left
        MD.motor_1(-power_step)
        MD.motor_2(-power_step)
        time.sleep(time_reverse)
        MD.stop()

        for a in range(1,10):#wall alignment via distance sensor
            dm = S.dm_2()
            MD.motor_1(+power1)#small right turn
            MD.motor_2(-power1)#small right turn
            time.sleep(0.3/a)
            MD.stop()
            if S.dm_2() > dm:
                MD.motor_1(-power1)#small left turn
                MD.motor_2(+power1)#small left turn
                time.sleep(0.3/a)
                MD.stop()

        MD.motor_1(power_turn)
        MD.motor_2(-power_turn)
        time.sleep(time_turn)
        MD.stop()

        for a in range(1,10):#wall alignment via distance sensor
            dm = S.dm_2()
            MD.motor_1(+power1)#small right turn
            MD.motor_2(-power1)#small right turn
            time.sleep(0.3/a)
            MD.stop()
            if S.dm_2() > dm:
                MD.motor_1(-power1)#small left turn
                MD.motor_2(+power1)#small left turn
                time.sleep(0.3/a)
                MD.stop()

        MD.motor_1(power_step)
        MD.motor_2(power_step)
        time.sleep(time_out_of_turn)
        MD.stop()
        but_1 = button1_status()
        but_2 = button2_status()
        dm = S.dm_2()
        print('button1: ',but_1,'button2:', but_2, 'distance: ', dm)

    time.sleep(0.2)

