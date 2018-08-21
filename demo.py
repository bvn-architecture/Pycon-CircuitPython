import sys
import os



""" Check Python implementation for testing purposes. """
if sys.implementation.name == 'circuitpython':
    import board
    pass

def main():
    """ event loop """
    while True:
        pass
if sys.implementation.name == 'circuitpython':
    main()
