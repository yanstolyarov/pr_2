import motor_driver as M
import time

t90 = 0.8
m1 = 30
m2 = 30
t270 = 2.1

M.motor_pwm_forw_1(m1)
M.motor_pwm_reverse_2(m2)

time.sleep(t90)

M.stop()

time.sleep(3)

M.motor_pwm_forw_1(m1)
M.motor_pwm_reverse_2(m2)
time.sleep(t270)

M.stop()
