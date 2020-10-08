from sense_emu import SenseHat

sense = SenseHat()

keydown = 0
keyup = 0
p = True
bool = False

while True:
    for event in sense.stick.get_events():
        
        if event.action is 'pressed' and (event.direction is 'up' or event.direction is 'down' or event.direction is 'left' or event.direction is 'right'):
            print(event, bool)
            if bool:
                sense.clear()
                if p:
                    for i in range(8):
                        sense.set_pixel(3, i, 0, 255, 255)
                    for i in range(7):
                        sense.set_pixel(i, 0, 0, 255, 255)
                else:
                    for i in range(8):
                        sense.set_pixel(0, i, 0, 255, 0)
                    for i in range(7):
                        sense.set_pixel(i, 0, 0, 255, 0)
                    for i in range(7):
                        sense.set_pixel(i, 3, 0, 255, 0)
                    for i in range(8):
                        sense.set_pixel(7, i, 0, 255, 0)
                    
                p = not p
            
            bool = not bool



