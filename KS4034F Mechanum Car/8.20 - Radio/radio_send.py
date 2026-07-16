from microbit import *
import radio

# Turn the radio on, and set the group to a channel 13.
radio.on()
radio.config(group=13)  # pick your own channel


# Enter your string here
s = "TURING"

# This is an index. It counts up each time the button is pressed. 
i = 0

while True:
    if button_a.is_pressed():
        # send the character at index i
        radio.send(s[i])

        # show the character on the display
        display.show(s[i])

        # print the index and the character to the serial console
        print("{} - {}".format(i, s[i]))

        # add one to the index, and wrap around (using modulo operator)
        i = (i+1) % len(s)

        # add a debounce to prevent multiple button presses from being registered
        sleep(500)