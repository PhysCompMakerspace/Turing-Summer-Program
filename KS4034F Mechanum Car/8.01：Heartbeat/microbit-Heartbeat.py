# A Hello World program for the micro:bit.
# It displays a pulsing heart on the LED display.

# Import all the built-in functions of the micro:bit library.
from microbit import *

# Set up an infinite loop that shows a large heart, then a small heart, then repeats.
while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
