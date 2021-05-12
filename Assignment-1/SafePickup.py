from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""

def main():
    #check for beeper, if found, pick it up or else do nothing
    check_beeper()

#when a beeer is found at current position, pick it up
def check_beeper():
     if beepers_present():
      pick_beeper()    

if __name__ == '__main__':
    run_karel_program('SafePickup2.w')
