#!/usr/bin/python3
''' itsOrD || netinterface '''


import netifaces


def main():
    # playing with networking in python on the ipad
    print(netifaces.interfaces())
    print(netifaces.interfaces())

    
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        print(netifaces.ifaddresses(i))    
    
if __name__ == "__main__":
    main()
