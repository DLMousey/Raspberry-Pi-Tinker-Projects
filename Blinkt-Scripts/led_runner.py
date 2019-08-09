import time, colorsys, random
from blinkt import set_brightness, set_pixel, show, clear

def displayColour(index, reverse):
    spacing = 360.0 / 16.0
    hue = 0
    
    if(reverse == False):
        if((x - 1) > -1):
            set_pixel(x - 1, 0, 0, 0)
            
        if(x != 7):
            set_pixel(7, 0, 0, 0)
    else:
        if((x + 1) < 8):
            set_pixel(x + 1, 0, 0, 0)
            
        if(x != 0):
            set_pixel(0, 0, 0, 0)
            
    hue = int(time.time() * 100) % 360
    
    offset = x * spacing
    h = ((hue + offset) % 360) / 360.0
    
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
    set_pixel(x, r, g, b)
    show()

set_brightness(0.05)

while True:
    for x in range(8):
        if x == 8:
            x = 0
                 
        displayColour(x, False)
    
    for x in reversed(range(8)):
        if x == 0:
            x = 0
            
        displayColour(x, True)