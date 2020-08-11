#!/usr/bin/python3
''' itsOrD || moving files with built in functions '''


import shutil
import os


# path for files in questions: /home/student/mywork/pythonWithAlta3/09Aug

SRC = '/home/student/mywork/pythonWithAlta3/09Aug'
DEST = '/home/student/mywork/pythonWithAlta3/09Aug/ceph_storage'


def main():
    ''' sc2 references for days '''
    os.chdir(SRC)
    shutil.move('raynor.obj', DEST)
    xname = input(f'''What's the new name you'd like to use for kerrigan.obj? ''')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()
