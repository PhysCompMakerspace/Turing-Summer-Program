from microbit import *
from IR_receiver_class import NECDecode
from keyes_mecanum_Car_V2 import *


nec = NECDecode(pin0)
mecanumCar = Mecanum_Car_Driver_V2()


while True:
    result = nec.decode_nec()
    
    addr, cmd = result if isinstance(result, tuple) else (None, None)
    if cmd is not None:
        nec.print_info()

    if cmd == 0x46:
        mecanumCar.Motor_Upper_L(1, 100)
        mecanumCar.Motor_Lower_L(1, 100)
        mecanumCar.Motor_Upper_R(1, 100)
        mecanumCar.Motor_Lower_R(1, 100)
        sleep(1000)
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
    elif cmd == 0x15:
        mecanumCar.Motor_Upper_L(0, 100)
        mecanumCar.Motor_Lower_L(0, 100)
        mecanumCar.Motor_Upper_R(0, 100)
        mecanumCar.Motor_Lower_R(0, 100)
        sleep(1000)
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
    elif cmd == 0x44:
        mecanumCar.Motor_Upper_L(0, 100)
        mecanumCar.Motor_Lower_L(0, 100)
        mecanumCar.Motor_Upper_R(1, 100)
        mecanumCar.Motor_Lower_R(1, 100)
        sleep(112)
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
    elif cmd == 0x43:
        mecanumCar.Motor_Upper_L(1, 100)
        mecanumCar.Motor_Lower_L(1, 100)
        mecanumCar.Motor_Upper_R(0, 100)
        mecanumCar.Motor_Lower_R(0, 100)
        sleep(112)
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)