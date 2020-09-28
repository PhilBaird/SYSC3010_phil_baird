from sense_emu import SenseHat
import time
#import keyboard


sense = SenseHat()

keydown = 0
keyup = 0
p = True

while True:
        time.sleep(1)
        sense.clear()
    #key = keyboard.read_key()
    #print( key )
    
    #if key == keydown || key == keyup:
        if p:
            for i in range(7):
                sense.set_pixel(i , 0 , 0 , 255 , 255)
            for i in range(8):
                sense.set_pixel(0 , i , 0 , 255 , 255)
            for i in range(7):
                sense.set_pixel(i , 3 , 0 , 255 , 255)
            for i in range(4):
                sense.set_pixel(7 , i , 0 , 255 , 255)
        else:    
            for i in range(7):
                sense.set_pixel(i , 0 , 0 , 255 , 0)
            for i in range(8):
                sense.set_pixel(0 , i , 0 , 255 , 0)
            for i in range(7):
                sense.set_pixel(i , 3 , 0 , 255 , 0)
            for i in range(8):
                sense.set_pixel(7 , i , 0 , 255 , 0)
            for i in range(7):
                sense.set_pixel(i , 7 , 0 , 255 , 0)
        p = not p
            
            
        
    