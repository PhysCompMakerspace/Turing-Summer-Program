# Pressing the A button will show the current heading of the micro:bit in degrees.

from microbit import *

# The matrix display will tell you to light up all the LEDs by moving the board around.
compass.calibrate()

while True:
    # press the button to show the heading from the compass in degrees.
    # 0 for North, 90 for East, 180 for South, and 270 for West
    if button_a.is_pressed():
        display.scroll(compass.heading())


