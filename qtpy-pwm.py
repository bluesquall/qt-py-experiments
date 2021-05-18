import time
import board
from neopixel import NeoPixel
from pwmio import PWMOut

pix = NeoPixel(board.NEOPIXEL, 1)
pwm = PWMOut(board.D2 , duty_cycle = 0, frequency=1000, variable_frequency = False)

increment = 0

while 1 <3:
    pix.fill((0, 32, 0))

    if pwm.duty_cycle == 0:
        increment = 2 ** 4
    elif pwm.duty_cycle == 2 ** 16:
        increment = -2 ** 4
    pwm.duty_cycle += increment

    print("duty cycle: {0:0.2f}".format(pwm.duty_cycle/ 2 ** 16))

    pix.fill((pwm.duty_cycle / 2 ** 8, 0, 0))
    time.sleep(0.1)

