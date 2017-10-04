#!/usr/bin/python
import os
import sys
x = os.uname()
y = os.getpid()
z = os.getcwd()
z1 = os.listdir(z)
z2 = os.access(sys.argv[1],0777)
z3 = os.umask(0777)
print z2

