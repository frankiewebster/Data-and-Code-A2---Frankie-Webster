from microbit import *
import music

# Prompt user to press A to begin task
display.scroll("Press A")

seconds = 0  # Initialise seconds
button_pressed = False  # Track when button A is pressed

def on_button_pressed_a():
    global seconds, button_pressed
    seconds = 0  # Reset seconds when button A is pressed
    button_pressed = True  # Set button pressed flag to True
    music.play(music.BA_DING)  # Play a starting sound

def on_forever():
    global seconds, button_pressed
        # Play power-up sound and display message at specific intervals
    if seconds == 30: 
        music.play(music.POWER_UP)  # Play power-up sound every 30 seconds
        display.scroll("CHANGE")
    if seconds == 60: 
        music.play(music.POWER_UP)  # Play power-up sound every 30 seconds
        display.scroll("CHANGE")
    if seconds == 90: 
        music.play(music.POWER_UP)  # Play power-up sound every 30 seconds
        display.scroll("CHANGE")
    if seconds == 120:
            music.play(music.DADADADUM)  # End sound at 120 seconds
            display.show(Image.SMILE)    # Show a smiley face
            button_pressed = False       # Stop the process

# Infinite loop to check button press and seconds
while True:
    if button_a.was_pressed(): 
        on_button_pressed_a()
    on_forever()
    sleep(100)  # Small delay
