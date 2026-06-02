from microbit import *
from keyes_mecanum_Car_V2 import *
import neopixel

# LED array
display.off()

# motors
mecanumCar = Mecanum_Car_Driver_V2()
mecanumCar.Motor_Upper_L(0, 0)
mecanumCar.Motor_Lower_L(0, 0)
mecanumCar.Motor_Upper_R(0, 0)
mecanumCar.Motor_Lower_R(0, 0)

# addressable LEDs
np = neopixel.NeoPixel(pin7, 4)
for i in range(4):
    np[i] = (0, 0, 0)
np.show()

# LEDs
mecanumCar.left_led(0)
mecanumCar.right_led(0)