from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    Move karel diagonally when the spot is a valid move and place the 
    beeper at the diagonal spots
    """
    while front_is_clear():
       place()
    place()  

#place beeper diagonally and move when it is valid
def place():
    put_beeper()
    if front_is_clear():
       move()
       if front_is_clear():
           move()
           turn_left()
           if front_is_clear():
               move()
               turn_right()
#turn karel right
def turn_right():
    turn_left()
    turn_left()
    turn_left()  

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
