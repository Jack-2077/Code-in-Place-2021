"""
Midpoint.py
Skip the first corner and drop beepers until a corner is reached and 
turn around and look for beepers at the other end and if present, pick it up and
go to opposite corner
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move()
        put_beeper()
    turn_around()
    while beepers_present():
        pick_beeper()
        move()
        while beepers_present():
           if front_is_clear() :
               move()
        turn_around()
        move()
    put_beeper()

def turn_around():
    turn_left()
    turn_left()
