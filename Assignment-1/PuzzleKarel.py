from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    move karel to pick up the beeper and place it inside 
    the puzzle and return back to initial starting spot
    """
    pick_up()
    place_beeper()
    to_initial()

#move and pick up the beeper
def pick_up():
   move()
   move()
   pick_beeper()
   
#place the beeper 
def place_beeper():
   move()
   turn_left()
   move()
   move()
   put_beeper()

#come back to initial position
def to_initial():
    turn_around()
    move()
    move()
    turn_around()
    turn_left()
    move()
    move()
    move()
    turn_around()
    
#turn karel around
def turn_around():
    turn_left()
    turn_left()
    

if __name__ == '__main__':
    run_karel_program('Puzzle.w')
