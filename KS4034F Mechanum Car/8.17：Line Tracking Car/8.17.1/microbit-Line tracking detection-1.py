# Reads the signal from the IR sensors on the front of the car.
# It lights up an LED to show when the left, center, or right sensor detects an object or line.

from microbit import *

display.off()

val_L = 0
val_C = 0
val_R = 0

while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    print("digital signal:", end = ' ')
    print(val_L, end = ' ')
    print(val_C, end = ' ')
    print(val_R)
    sleep(200)
