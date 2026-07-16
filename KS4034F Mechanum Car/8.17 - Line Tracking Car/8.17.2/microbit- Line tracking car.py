from microbit import *
from keyes_mecanum_car_v2 import *
mecanumCar = Mecanum_Car_Driver_V2()
display.off()

val_L = 0
val_C = 0
val_R = 0

speed = 40

while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    if val_C == 0:
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, speed)
            mecanumCar.Motor_Lower_L(1, speed)
            mecanumCar.Motor_Upper_R(0, speed)
            mecanumCar.Motor_Lower_R(0, speed)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, speed)
            mecanumCar.Motor_Lower_L(0, speed)
            mecanumCar.Motor_Upper_R(1, speed)
            mecanumCar.Motor_Lower_R(1, speed)
        else:
            mecanumCar.Motor_Upper_L(0, 0)
            mecanumCar.Motor_Lower_L(0, 0)
            mecanumCar.Motor_Upper_R(0, 0)
            mecanumCar.Motor_Lower_R(0, 0)
    else :
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, speed)
            mecanumCar.Motor_Lower_L(1, speed)
            mecanumCar.Motor_Upper_R(0, speed)
            mecanumCar.Motor_Lower_R(0, speed)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, speed)
            mecanumCar.Motor_Lower_L(0, speed)
            mecanumCar.Motor_Upper_R(1, speed)
            mecanumCar.Motor_Lower_R(1, speed)
        else:
            mecanumCar.Motor_Upper_L(1, speed)
            mecanumCar.Motor_Lower_L(1, speed)
            mecanumCar.Motor_Upper_R(1, speed)
            mecanumCar.Motor_Lower_R(1, speed)

