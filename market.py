#!/usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by Ceyhun Alyeşil (ceyhunalyesil@gmail.com)
#license:gplv3

from pysqlite2 import dbapi2 as sqlite
import sys

#well this file will include our market's functions. first of all at the market we should have a list of item prices
#second we should have items and list of their cost. normally i could prefer to save this data at db. but donno we will try
#lets first save it on a list or dictionary than we can transfer this values to db if it become nessecary.
item_prices = {"wolfblood":30, "crowfeather":10, "spoison":40, "tfur":70, "bfur":70, "gdust":1, "fang":90, "vdust":100, "soulgem":1000} 
helmets = {"dragon_helmet":1000, "leather_cap":50}
armors = {"plate_armor":1000, "leather_armor":100}
shields = {"iron_shield":500, "wood_shield":100}

#item clases will continue like this but we have to add their stat points to a db. than take these values and add them to
#the battle mechanics.
class market:
	def __init__(self):
		self.connection = sqlite.connect('test.db')
		memoryConnection = sqlite.connect(':memory:')
		self.cursor = self.connection.cursor()

	def welcomeToMarket(self):
		print "Greetings your hero. This is our town's market. You can sell and buy goods here. We dont have much items,"
		print "you know these is hard times we have because of war. But in the future, ofcourse with your help we can make"
		print "better work. Now what you want?"
		print "To view what items you have type W"
		print "To sell all your items type S"
		print "To view what we have at the market just type M"
		youwant = raw_input("What you want: ")
		youwant = str(youwant)
	
		W = "W"
		S = "S"
		M = "M"

		if youwant == W:
			self.viewItems()
		elif youwant == S:
			self.sellYourItems()
		elif youwant == M:
			self.viewMarket()
		else:
			sys.exit()

	def viewItems(self):	
		self.cursor.execute('SELECT * FROM stash WHERE number > 0')
		row = self.cursor.fetchone()
		for row in self.cursor:
			print "Item:", row[1]
			print "You have:", row[2]
	
	def sellYourItems(self):
		self.cursor.execute('SELECT * FROM stash WHERE number > 0')
		row = self.cursor.fetchone()
		for row in self.cursor:
			price = item_prices[row[1]]
			total_income = price * int(row[2])
			self.cursor.execute('SELECT * FROM gold')
			bow = cursor.fetchone()
			gold = bow[1] + total_income
			self.cursor.execute('UPDATE gold SET golhave=?', (gold))
			self.connection.commit()
			print "You sold all of your %s" %row[1]
			print "you gained %s gold" %total_income

	def viewMarket():
		return welcomeTomarket()
market = market()
market.welcomeToMarket()
