# Display an image on the micro:bit every 500 ms and send a value to the
# serial port every 1000 ms. This is done in a non-blocking way, so that both
# tasks can run at the same time. It avoids using "sleep()" which would block
# the execution of the program and prevent the other task from running.


from microbit import *
import time

img_1 = Image("90000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
img_2 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00009")

# set the initial time
# time.ticks_ms() returns the number of milliseconds since the micro:bit was turned on
now_1 = time.ticks_ms()
now_2 = time.ticks_ms()

# set a flag to toggle the display
toggle_1 = True

# set a counter to send to the serial port
i = 0


while True:
    # change the display every 500 ms
    if time.ticks_diff(time.ticks_ms(), now_1) >= 500:
        # update the time
        now_1 = time.ticks_ms()
        # toggle the display
        if toggle_1:
            display.show(img_1)
        else:
            display.show(img_2)
        toggle_1 = not toggle_1
        
    # send a value to the serial port every 1000 ms
    if time.ticks_diff(time.ticks_ms(), now_2) >= 1000:
        # update the time
        now_2 = time.ticks_ms()
        # send the value of i to the serial port
        print(i)
        # increase i by 1
        i = i + 1
        