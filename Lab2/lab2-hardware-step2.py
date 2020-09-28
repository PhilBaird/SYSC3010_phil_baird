from sense_emu import SenseHat

sense = SenseHat()

while True:
    temp = sense.get_temperature()

    if temp >= 20:
        sense.set_pixels([(255, 0, 0) for i in range(64)])
else:
    sense.set_pixels([(0, 0, 255) for i in range(64)])