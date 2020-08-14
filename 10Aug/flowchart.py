#!/usr/bin/python3
''' itsOrD || working on basic loop exit conditions'''


## NOTE this does not work as expected. Loop maintains itself rather than exiting
## TODO: fix if checks


from subprocess import call
from os import name as osname
import sys


EXIT = False


def clean_prompt(prompt_str):
    # simplify/clean user answers to prompts
    ans = input(prompt_str)
    ans = ans.lower().lstrip().rstrip()
    if ans in ['q', 'quit', 'exit']:
        EXIT = True
        print('now we in exit condition with EXIT=', EXIT)
    print('ans: ', ans)
    return ans


def clear():
    # check and make call for specific operating system
    _ = call('clear' if osname =='posix' else 'cls')


def main():
    ''' looping flowchart '''
    
    while EXIT is False:
        # ans = input('Choose yes or no')
        print('in loop with EXIT=', EXIT)
        while clean_prompt('Choose yes or no: ') not in ['yes', 'y', 'no', 'n']:
            print('about to call main again... EXIT=', EXIT)
            main()
    sys.exit()
        
        
    
    
if __name__ == "__main__":
    main()
    
