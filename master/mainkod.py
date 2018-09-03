import motor_driver as MD
import time
import serial1 as S

while 1:
  MD.motor_pwm_forw_1(25)
  MD.motor_pwm_forw_2(20)
  time.sleep(0.15)
  dalnomer1 = S.dm_1()
  dalnomer2 = S.dm_2()
  print('dalnomer1', dalnomer1)
  print('dalnomer2', dalnomer2)

  if dalnomer1 < 20:
    dalnomer2 = S.dm_2()
    if dalnomer2 > 25:
      MD.motor_pwm_forw_2(50)
      MD.motor_pwm_reverse_1(50)
      time.sleep(0.5)
      MD.stop()
      dalnomer1 = S.dm_1()
      dalnomer2 = S.dm_2()
      print('dalnomer1', dalnomer1)
      print('dalnomer2', dalnomer2)
      if dalnomer1 > 20:
        MD.all_motor_pwm_forward(30)
        time.sleep(3)
        dalnomer1 = S.dm_1()
        if dalnomer1 < 10:
          MD.stop()

    else:
      
      MD.motor_pwm_forw_1(50)
      MD.motor_pwm_reverse_2(50)
      time.sleep(0.5)
      MD.stop()
      dalnomer1 = S.dm_1()
      dalnomer2 = S.dm_2()
      print('dalnomer1', dalnomer1)
      print('dalnomer2', dalnomer2)
      if dalnomer1 > 20:
        MD.all_motor_pwm_forward(30)
        time.sleep(3)
        dalnomer1 = S.dm_1()
        if dalnomer1 < 10:
          MD.stop()
          dalnomer1 = S.dm_1()
          dalnomer2 = S.dm_2()
          print('dalnomer1', dalnomer1)
          print('dalnomer2', dalnomer2)
      else:

        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(50)
        time.sleep(0.5)
        MD.stop()
        MD.all_motor_pwm_forward(30)
        time.sleep(3)
        dalnomer1 = S.dm_1()
        if dalnomer1 < 10:
          MD.stop()
          dalnomer1 = S.dm_1()
          dalnomer2 = S.dm_2()
          print('dalnomer1', dalnomer1)
          print('dalnomer2', dalnomer2)

  else:
    dalnomer1 = S.dm_1()
    dalnomer2 = S.dm_2()
    print('dalnomer1', dalnomer1)
    print('dalnomer2', dalnomer2)

    if dalnomer2 > 25:
      MD.stop()
      MD.motor_pwm_forw_2(50)
      MD.motor_pwm_reverse_1(50)
      time.sleep(0.5)
      MD.stop()
      dalnomer1 = S.dm_1()
      dalnomer2 = S.dm_2()
      print('dalnomer1', dalnomer1)
      print('dalnomer2', dalnomer2)
      if dalnomer1 > 20:
        MD.all_motor_pwm_forward(30)
        time.sleep(3)
        dalnomer1 = S.dm_1()
        if dalnomer1 < 10:
          MD.stop()
          dalnomer1 = S.dm_1()
          dalnomer2 = S.dm_2()
          print('dalnomer1', dalnomer1)
          print('dalnomer2', dalnomer2)
  if dalnomer1 < 10:
    MD.all_motor_pwm_reverse(30)
    time.sleep(1)
    MD.stop()
