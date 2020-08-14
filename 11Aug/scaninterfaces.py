#!/usr/bin/python3
''' itsOrD || '''


from linux_nethelp.scan_interfaces import ScanInterfaces

import pprint

interfaces = list( ScanInterfaces() )


def main():
    '''  '''
    print(interfaces)
    
if __name__ == "__main__":
    main()
