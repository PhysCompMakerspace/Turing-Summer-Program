from microbit import Image, display, button_a, button_b, sleep

# check to see if you have the speech module available (only on micro:bit V2)
try:
    from speech import say
    HAS_SPEECH = True
    display.show(Image("00000:""00009:""00090:""90900:""09000"))
except ImportError:
    HAS_SPEECH = False
    display.show(Image("90000:""09000:""00909:""00090:""00009"))

sleep(2000)

# Function to say a sentence
def speak(text):
    display.show("*")
    if HAS_SPEECH:
        say(text)
    else:
        display.scroll("V2 ONLY")
    display.clear()

# Function for multiple words with pauses
def speak_slowly(words, pause_ms=500):
    for word in words:
        speak(word)
        sleep(pause_ms)

current = 0

# lists the phrases you want to speak.
phrases = [
    "Hello world",
    "Do re mi fa so",
    ["T", "U", "R", "I", "N", "G"],
    "Program your microbit to speak"
]

while True:
    display.show(current)
    
    if button_a.was_pressed():
        if isinstance(phrases[current], list):
            speak_slowly(phrases[current])
        else:
            speak(phrases[current])
    
    if button_b.was_pressed():
        current = (current + 1) % len(phrases)
    
    sleep(100)