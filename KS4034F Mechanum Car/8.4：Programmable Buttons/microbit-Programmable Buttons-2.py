# This displays something on the screen that scrolls up or down depending on which button is pressed.

from microbit import *

# set up variables and custom images
a = 0
val1 = Image("00000:""00000:""00000:""00000:""90009")
val2 = Image("00000:""00000:""00000:""90009:""36963")
val3 = Image("00000:""00000:""90009:""36963:""66966")
val4 = Image("00000:""90009:""36963:""66966:""99999")
val5 = Image("90009:""36963:""66966:""99999:""99999")
val6 = Image("36963:""66966:""99999:""36963:""09990")
val7 = Image("66966:""99999:""36963:""09990:""00000")

# display the first image
display.show(val1)

# enter a loop to check for button presses and update the display accordingly
while True:
    # Debounce the button: enter a loop to check for button A being pressed
    while button_a.is_pressed() == True:
        sleep(10)
        # when button A is released, increment the variable a and break out of the debounce loop
        if button_a.is_pressed() == False:
            a = a + 1
            # don't let a go above 6
            if(a >= 6):
                a = 6
            break
    # do the same for button B, but decrement a instead of incrementing it
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break

    # check the value of a and display the corresponding image
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
    if a == 6:
        display.show(val7)
