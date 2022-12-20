def on_gesture_shake():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_icon(IconNames.YES)
    basic.pause(100)
basic.forever(on_forever)
