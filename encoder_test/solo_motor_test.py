from RPi import GPIO
import time

e2 = 17#inc
m2 = 27#ind
enb = 4

GPIO.setwarnings(False)

GPIO.setmode (GPIO.BCM)

GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

#To create a PWM instance: p = GPIO.PWM(channel, frequency)
p_w = GPIO.PWM(enb,100)

p_w.start(0)


def motor(x):
    if x > 0:
        p_w1.ChangeDutyCycle(x)
        GPIO.output(e2, GPIO.HIGH)
        GPIO.output(m2, GPIO.LOW)
    if x < 0:
        p_w1.ChangeDutyCycle(-x)
        GPIO.output(m2, GPIO.HIGH)
        GPIO.output(e2, GPIO.LOW)

while 1:
    motor(20)
    time.sleep(3)
    motor(-60)
    time.sleep(3)
    motor(99)
    time.sleep(3)
    motor(0)