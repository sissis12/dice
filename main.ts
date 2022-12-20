input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
})
