from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    """
    check for beepers in the missing colomun and add beepers in the missing spots,
    move towards missing columns from start of the current column
    """
    turn_left()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()
    else:
         while front_is_clear():
            place_beepers()
            to_column_start()
            if front_is_clear():
                to_next_column()
                if no_beepers_present():
                    put_beeper() 
                turn_left()
                if front_is_blocked():
                    turn_right()
                    if front_is_clear():
                        to_next_column()
                        turn_left()  
#place if placement of beeper is vlaid
def place_beepers():
    while front_is_clear():
         check_beeper()  
    check_beeper()

#move towards the start(bottom) of the colomun 
def to_column_start():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()    

#make karel turn right
def to_next_column():            
     move()
     move()
     move()
     move() 

#check for beepers in coloumn and move up front, if no beeper is present, place beeper
def check_beeper():
    if beepers_present():
        if front_is_clear():
            move()
    else:
        put_beeper()   

#make karel turn right
def turn_right():
    turn_left()  
    turn_left()  
    turn_left()            

    

if __name__ == '__main__':
    run_karel_program('1x1.w')
