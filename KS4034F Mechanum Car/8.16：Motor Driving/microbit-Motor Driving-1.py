# This code demonstrates how to drive the motors using the micro:bit.
# Add the keyes_mecanum_Car_V2 library to your project.
#   In python.microbit.org/v/3, click on "Project" in the lower left.
#   "Create file" and name it "keyes_mecanum_Car_V2.py".
#   Copy the code from "keyes_mecanum_Car_V2.py" in this repository and paste it into the new file you created.
#   Do this process each time you want to use the motor library in a new project.
# Copy the code below into "main.py"

from microbit import *
from keyes_mecanum_Car_V2 import *

# create a Mecanum_Car_Driver_V2 class object to control the motors of the mecanum car.
# This lets you use the methods in the class to easily control the motors of the car.
# An example of a method is ".Motor_Upper_L()", which controls the upper left motor of the car.
# The first argument of the method is the direction of the motor (0 for forward, 1 for backward).
# The second argument of the method is the speed of the motor (0-100).
mecanumCar = Mecanum_Car_Driver_V2()

# set the speed of the motors.
speed = 80

while True:
    display.show(Image.ARROW_S)
    mecanumCar.Motor_Upper_L(1, speed)
    mecanumCar.Motor_Lower_L(1, speed)
    mecanumCar.Motor_Upper_R(1, speed)
    mecanumCar.Motor_Lower_R(1, speed)
    sleep(1000)
    display.show(Image.ARROW_N)
    mecanumCar.Motor_Upper_L(0, speed)
    mecanumCar.Motor_Lower_L(0, speed)
    mecanumCar.Motor_Upper_R(0, speed)
    mecanumCar.Motor_Lower_R(0, speed)
    sleep(1000)
    display.show(Image.ARROW_E)
    mecanumCar.Motor_Upper_L(0, speed)
    mecanumCar.Motor_Lower_L(0, speed)
    mecanumCar.Motor_Upper_R(1, speed)
    mecanumCar.Motor_Lower_R(1, speed)
    sleep(1000)
    display.show(Image.ARROW_W)
    mecanumCar.Motor_Upper_L(1, speed)
    mecanumCar.Motor_Lower_L(1, speed)
    mecanumCar.Motor_Upper_R(0, speed)
    mecanumCar.Motor_Lower_R(0, speed)
    sleep(1000)
    display.show(Image("00900:""09990:""99999:""99999:""09090"))
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    sleep(1000)
