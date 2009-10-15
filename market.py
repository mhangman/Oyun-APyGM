#!/usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by Ceyhun Alyeşil (ceyhunalyesil@gmail.com)
#license:gplv3

from pysqlite2 import dbapi2 as sqlite
import sys

#well this file will include our market's functions. first of all at the market we should have a list of item prices
#second we should have items and list of their cost. normally i could prefer to save this data at db. but donno we will try
#lets first save it on a list or dictionary than we can transfer this values to db if it become nessecary.

def welcomeToMarket():
	print """Greetings your hero. This is our town's market. You can sell and buy goods here. We dont have much items,
	you know these is hard times we have because of war. But in the future, ofcourse with your help we can make
	better work. Now what you want?"""
	print "To view what items you have type W"
	print "To sell all your items type S"
	print "To view what we have at the market just type M"
	youwant = raw_input("What you want: ")
	youwant = str(youwant)
	
	W = "W"
	S = "S"
	M = "M"

	if youwant == W:
		viewItems()
	elif youwant == S:
		sellYourItems()
	elif youwant == M:
		viewMarket()
	else:
		sys.exit()

def viewItems():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM stash')
	row = cursor.fetchall()
	for row in cursor:
		print "Item:", row[1]
		print "You have:", row[2]
	return welcomeToMarket()

def sellYourItems():
	return welcomeToMarket()

def viewMarket():
	return welcomeTomarket()