#!/usr/bin/python3
''' itsOrD || Pythonic RegEx practice '''


import urllib.request
import re
import sys


def main():
    # prompt for a search location and search there
    print('''\nNew search:  [press 'q' to quit at any time!]''')

    url = input('Where should we search?  ')
    if url in ['q', 'quit', 'exit']:
        sys.exit()

    phrase = input('What phrase are we looking for?  ')
    if phrase in ['q', 'quit', 'exit']:
        sys.exit()

    searchMe = urllib.request.urlopen(url).read().decode('utf-8')

    if re.search(phrase, searchMe):
        print('Found a match!')
    else:
        print('No mactches found...')
    

if __name__ == "__main__":
    while True:
        main()
