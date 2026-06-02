# Create a 5x5 LED pattern on the micro:bit's matrix display.

from microbit import *

# An arrow pointing down.
val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
