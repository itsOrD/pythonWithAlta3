#!/usr/bin/python3

from time import sleep
from random import randint
from asciimatics.screen import Screen

def welcome(screen):
    for i in range(1,3696):
        screen.print_at('Welcome to Nap-Landius!!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

def welcome_screen():
    Screen.wrapper(welcome)

'''
def death(screen):
    screen.print_at('You have died of exhaustion.\n Better luck napping next time!', 0, 0, COLOUR_GREEN, A_BOLD)


def death_screen():
    Screen.wrapper(basic)
'''
