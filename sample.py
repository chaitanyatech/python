#!/usr/bin/python

import os
import sys 
import errno
import shutil
'''
#make a directory using try catch to get tthe error type

path = sys.argv[1]
try:
    os.makedirs(path,0755)
except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

#make a directory with if else

path = sys.argv[1]
if not os.path.exists(path):
    os.makedirs(path, 0755)
    print "the directory is created"

else:
    print "This Directory already exists"

'''
# copying the file

path = sys.argv[1]
path1 = sys.argv[2]
if os.path.exists(path):
    shutil.copy(path,path1)
    print "the file is copied to new path"
else:
    print"no file sxist such"
    
