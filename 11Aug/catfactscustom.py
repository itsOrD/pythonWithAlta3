#!/usr/bin/python3
''' itsOrD || requests API practice in Python '''

import requests
import pprint

def main():
    # pull some cat facts and manipulate the data before printing
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    r = r.json()
    #print(pprint.pprint(r))
    
    maxVote = 0
    for fact in r['all']:
        #print(fact['upvotes'])
       if fact['upvotes'] > maxVote:
           maxVote = fact['upvotes']

    print('highest voted cat fact amount --> ', maxVote)


if __name__ == "__main__":
    main()
