from microbit import *
import radio

radio.on()
radio.config(group=13)

while True:
    message = radio.receive()

    if message:
        if len(message) == 1:
            # display a single character
            display.show(message)
        else:
            # display a longer message
            display.scroll(message)
