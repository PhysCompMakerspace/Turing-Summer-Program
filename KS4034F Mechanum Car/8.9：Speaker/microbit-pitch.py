# Plays a series of ascending pitches when Button A is pressed.

from microbit import *
import music

freq = 80

while True:
    while button_a.is_pressed():
        music.pitch(freq, duration=100)
        freq += 20
        if freq > 350:
            freq = 80
        sleep(100)
