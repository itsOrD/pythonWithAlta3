#!/usr/bin/python3
''' itsOrD || simple text based adventure with Python '''

from os import system, name
import pprint
from my_asciimatics import welcome_screen 


player_name = 'adventurer'
dashboard = {}


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def intro():
    global player_name 
    player_name = input('''Hello adventurer!  What is your name? \n >  ''') 
    print(''' \n Welcome to Nap-Landius. \n The land of competitive napping. \n  Your task in this world is to take the best possible nap.  \n Do you have what it takes?  Let's find out... \n''')


def init():
    global dashboard, player_name
    dashboard = {
            'Inventory': [],
            'Health': 100,
            'Energy': 6,
            'Name': player_name
        }


def show_dashboard():
    #for pair in dashboard.items():
    #    print(pair)
    for category in dashboard:
        print(f''' *** {category}: {dashboard[category]}''')
    print('\n')


def main():
    # simple gameplay to take a nap
    clear()
    init()
    intro()
    welcome_screen()
    show_dashboard()



if __name__ == "__main__":
    main()
