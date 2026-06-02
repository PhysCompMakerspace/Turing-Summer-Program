# Light up an LED on the matrix display.

from microbit import *

# Each "Image" is a 5x5 grid of numbers, 
# where each number represents the brightness of the corresponding LED.
# The numbers can range from 0 (off) to 9 (fully on).
# Each row of the grid is separated by a colon ":".
val1 = Image("90000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00900:""00000:""00000:")
val3 = Image("00000:""00000:""00000:""00000:""00009:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
