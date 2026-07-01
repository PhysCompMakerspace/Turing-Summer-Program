# Display characters and images on the micro:bit's 5x5 LED matrix.
# There is no infinite loop in this program,
# so it will run once then stop.

from microbit import *


# display single characters
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)


# display a custom image
# each set of 5 digits represents a row of the 5x5 LED matrix, with 0 for off and 9 on at 100% brightness
val = Image("00900:""00900:""90909:""09990:""00900")
display.show(val)
sleep(500)


# scroll a string across the display
display.scroll("hello!")
sleep(200)


# display built-in images
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)


# display each character in a string one at a time using a loop
s = "Turing"
for letter in s:
    display.show(letter)
    sleep(500)


# clear the display
display.clear()
