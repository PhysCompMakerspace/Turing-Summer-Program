# Play sounds with different pitches based on the distance detected by the ultrasonic sensor.

from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
import music

distance_val = 0

while True:
    distance_val = mecanumCar.get_distance()
    print("distance:", distance_val)
    if distance_val < 10:
        # music.play(tune)
        music.pitch(50*distance_val, duration=100)
        sleep(50)