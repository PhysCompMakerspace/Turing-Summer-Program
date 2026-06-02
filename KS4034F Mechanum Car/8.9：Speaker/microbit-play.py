from microbit import display, sleep, button_a
import music

all_tunes = [
    ("DADADADUM", music.DADADADUM),
    ("ENTERTAINER", music.ENTERTAINER),
    ("PRELUDE", music.PRELUDE),
    ("ODE", music.ODE),
    ("NYAN", music.NYAN),
    ("RINGTONE", music.RINGTONE),
    ("FUNK", music.FUNK),
    ("BLUES", music.BLUES),
    ("BIRTHDAY", music.BIRTHDAY),
    ("WEDDING", music.WEDDING),
    ("FUNERAL", music.FUNERAL),
    ("PUNCHLINE", music.PUNCHLINE),
    ("BADDY", music.BADDY),
    ("PYTHON", music.PYTHON),
    ("CHASE", music.CHASE),
    ("BA_DING", music.BA_DING),
    ("WAWAWAWAA", music.WAWAWAWAA),
    ("JUMP_UP", music.JUMP_UP),
    ("POWER_UP", music.POWER_UP),
    ("JUMP_DOWN", music.JUMP_DOWN),
    ("POWER_DOWN", music.POWER_DOWN),
]

while True:
    for name, tune in all_tunes:
        # wait for button A to be pressed
        while not button_a.is_pressed():
            sleep(10)

        # Display the first letter of the tune's name
        display.show(name[0])
        
        # Play the tune
        music.play(tune)
        
        sleep(200)