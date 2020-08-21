#!/usr/bin/python3
''' itsOrD || implementing asyncio on multiple functions '''

import asyncio
import sys
import time
import emoji
import curses
import colorama
from termcolor import colored
from os import system, name

ghost = emoji.emojize(":ghost:")
ghost_str = str(ghost)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def whole_screen_bar(window):
    # not working as intended, str'ing ghost seems unhelpful
    for i in range (50):
        window.addstr(10, 10, "[" + (f"{ghost}" * i) + ">" + (" " * (50 - i)) + "]")
        window.refresh()
        time.sleep(0.5)

def setup_terminal():
    print(colored("Let's fizz some buzzes!!", 'red', 'on_white'))

async def fizz():
    await asyncio.sleep(.1)
    case = "fizz"
    print("{:>10}".format(case))

async def buzz():
    await asyncio.sleep(.1)
    print(f'''{'buzz'.rjust(10)}''')

async def fizzbuzz():
    await asyncio.sleep(.1)
   # ghost = emoji.emojize(" :ghost: ")
    for i in range(11):
        sys.stdout.write("\r{0}>".format(ghost *i))
        sys.stdout.flush()
        time.sleep(0.3)
    print()

async def buzzfizz():
    await asyncio.sleep(.1)
    for i in range(100):
        window.addstr

async def main():
    clear()
    setup_terminal()
    task_f = asyncio.create_task(fizz())
    task_b = asyncio.create_task(buzz())
    task_fb = asyncio.create_task(fizzbuzz())
    await asyncio.gather(task_f, task_b, task_fb)
    input('Press enter to get more spooked!')
    curses.wrapper(whole_screen_bar)


if __name__ == "__main__":
    asyncio.run(main())
    
