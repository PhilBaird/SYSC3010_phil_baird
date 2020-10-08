from sense_emu import SenseHat

sense = SenseHat()

keydown = 0
keyup = 0
p = True
bool = False

while True:
    for event in sense.stick.get_events():
        print(event)
        if event.action == 'pressed' &  event.direction == 'left' :
            if bool:
                if p:
                    for i in range(7):
                        sense.set_pixel(i, 3, 0, 255, 255)
                    for i in range(7):
                        sense.set_pixel(i, 7, 0, 255, 255)
                else:
                    for i in range(7):
                        sense.set_pixel(i, 0, 0, 255, 0)
                    for i in range(7):
                        sense.set_pixel(i, 3, 0, 255, 0)
                    for i in range(8):
                        sense.set_pixel(7, i, 0, 255, 0)
                    for i in range(7):
                        sense.set_pixel(i, 7, 0, 255, 0)
                p = not p
            else:
                bool = not bool



