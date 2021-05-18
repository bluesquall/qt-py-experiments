import time
from math import pi, sin

import board
from analogio import AnalogOut

ao = AnalogOut(board.A0)

f = 2 # Hz

while 1 <3:
    ao.value = int(65535 * 0.5 * (1 + sin(2 * pi * f * time.monotonic())))
