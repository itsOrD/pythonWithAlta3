#!/usr/bin/python3
''' itsOrD || practice with Python dictionaries '''

def main():
    '''playing with get'''
    ## create a dictionary
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display parts of the dictionary
    print( switch["hostname"] )
    print( switch["ip"] )

    ## request a 'fake' key
    # print( switch["lynx"] )   # Be sure to comment out this line,
                            # or your program will CONTINUE to fail!
                            # if a KEY is requested that does not exist,
                            # an ERROR will be thrown!

    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get("lynx") )

    print( "Second test - .get()" )
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()" )
    print( switch.get("version") )

    print( "Fourth test - .keys()" )
    print( switch.keys() )

    print( "Fifth test - .values()" )
    print( switch.values() )

    print( "Sixth test - .pop()" )
    switch.pop("version") # removes this key (and value) pair
    print( switch.keys() )   # notice the value of version is gone
    print( switch.values() ) # notice the value 1.2

    print( "Seventh test - ADD a new value" )
    switch["adminlogin"] = "karl08"
    print( switch.keys() )
    print( switch.values() )

    print( "Eighth test - ADD a new value" )
    switch["password"] = "qwerty"
    print( switch.keys() )
    print( switch.values() )



if __name__ == "__main__":
    main()
