# This uses the LED Matrix to detect light intensity.
# LEDs can act as a photodiode, which means that they can detect light.
# Light falling on the LED will generate a small current, which can be measured to determine the light intensity.
# This works because the LED is connected to one of the analog-to-digital converters (ADC) on the micro:bit.

from microbit import *

while True:
    lightintensity = display.read_light_level()
    print("Light intensity:", lightintensity)
    sleep(100)
