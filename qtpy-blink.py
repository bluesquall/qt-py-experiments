import time
import board
from neopixel import NeoPixel

pix = NeoPixel(board.NEOPIXEL, 1)

while 1 <3:
    pix.fill((255, 0, 0))
    time.sleep(0.5)
    pix.fill((0, 0, 0))
    time.sleep(0.5)
