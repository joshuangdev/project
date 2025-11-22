def on_button_pressed_a():
    if fell == 1:
        basic.show_string("Ok, but remember, our system is not a toy, I can really call help!")
    else:
        basic.show_string("Our system is not a toy, I can really call help!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def timer2(last: number):
    global timer
    timer = last
    basic.pause(1000)
    basic.show_number(timer)
    timer += -1
    if timer == 0:
        pass
    else:
        timer2(last - 1)

def on_button_pressed_b():
    if fell == 1:
        music.play_tone(988, music.beat(BeatFraction.BREVE))
    else:
        basic.show_string("Ok, but remember, our system is not a toy, I can really call help!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global fell
    fell = 1
    basic.show_string("Press A if you're fine else press B if you can")
    timer2(10)
    fell = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

timer = 0
fell = 0
fell = 0