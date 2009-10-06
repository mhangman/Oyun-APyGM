#!usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by Ceyhun Alyeşil (ceyhunalyesil@gmail.com)
#license:gplv3

import sys
from mounster import *

#main gm screen
print "You must create tables before to start adding mounster type D if you want so"
print "To add Mounster to DB write M to quit this script just write Q"
print "To view mounsters just type W"
edit = raw_input("Type here: ")
data = str(edit)
M = "M"
Q = "Q"
W = "W"
D = "D"
U = "U"
if data == M:
	addMounster()
elif data == Q:
	sys.exit()
elif data == W:
	viewMounster()
elif data == D:
	npcDB()
elif data == U:
	updateMounster()

