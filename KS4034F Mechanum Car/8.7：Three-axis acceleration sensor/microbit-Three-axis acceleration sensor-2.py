# Print the x, y, and z acceleration values from the micro:bit's 
# three-axis acceleration sensor to the serial console.

from microbit import *

while True:
    # read the accelerometer values
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    # print to the serial console
    print("x, y, z:", x, y, z)

    sleep(100)
