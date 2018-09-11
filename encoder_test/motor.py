from RPi import GPIO
import time

#left
e1 = 27#digital
m1 = 18#digital
ena = 13#pwm

#right
e2 = 6#digital
m2 = 12#digital
enb = 19#pwm

#GPIO.setwarnings(False)

GPIO.setmode (GPIO.BCM)

GPIO.setup(e1,GPIO.OUT)
GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

#To create a PWM instance: p = GPIO.PWM(channel, frequency)
p_w1 = GPIO.PWM(ena,100)
p_w2 = GPIO.PWM(enb,100)

p_w1.start(0)
p_w2.start(0)

def motor_1(x):
    if x > 0:
        p_w1.ChangeDutyCycle(x)
        GPIO.output(e1, GPIO.HIGH)
        GPIO.output(m1, GPIO.LOW)
    if x < 0:
        p_w1.ChangeDutyCycle(-x)
        GPIO.output(m1, GPIO.HIGH)
        GPIO.output(e1, GPIO.LOW)

def motor_2(x):
    if x > 0:
        p_w1.ChangeDutyCycle(x)
        GPIO.output(e2, GPIO.HIGH)
        GPIO.output(m2, GPIO.LOW)
    if x < 0:
        p_w1.ChangeDutyCycle(-x)
        GPIO.output(m2, GPIO.HIGH)
        GPIO.output(e2, GPIO.LOW)
