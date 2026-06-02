# Displays a heart on the matrix display if the processor temperature
# is above 30 degrees Celsius, and a small heart otherwise.

from microbit import *

while True:

    if temperature() >= 30:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
