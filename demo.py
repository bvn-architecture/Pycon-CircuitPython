import sys
import os
import time

import board
import analogio

light = analogio.AnalogIn(board.LIGHT)


""" Check Python implementation for testing purposes. """
if sys.implementation.name == 'circuitpython':
    pass

def main():
    """ event loop """
    while True:
        print(light.value)
        time.sleep(0.1)
if sys.implementation.name == 'circuitpython':
    main()
