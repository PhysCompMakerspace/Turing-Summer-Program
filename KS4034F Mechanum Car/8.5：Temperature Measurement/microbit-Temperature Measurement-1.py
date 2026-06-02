# Reads the temperature from the micro:bit's built-in temperature sensor.
# This is not the air temperature, but rather the temperature of the processor.

from microbit import *


while True:
    # get the temperature reading from the micro:bit's built-in temperature sensor and print it to the console
    celsius = temperature()
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature:", celsius, "C,", fahrenheit, "F")
    
    # flash a progress animation across the LED matrix to show time passing
    for x in range(5):
        display.clear()
        for y in range(5):
            display.set_pixel(x, y, 9)
        sleep(200)

    display.clear()
    sleep(300)
