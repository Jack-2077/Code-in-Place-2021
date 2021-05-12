from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""

def main():
    """
    #check if the next move is valid, 
    then move up front and if a beeper is present, 
    pick it up
    """
    check_beeper()

#check if the next move is valid, then move up front and when there is a beeper, pick it up
def check_beeper():
 while front_is_clear(): 
        move()
        if beepers_present():
            pick_beeper()   

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
