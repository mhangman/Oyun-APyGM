#!/usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by Ceyhun Alyeşil (ceyhunalyesil@gmail.com)
#license:gplv3

from pysqlite2 import dbapi2 as sqlite
import sys

#this for adding mounsters
class gm_master:
	def __init__(self):
		self.connection = sqlite.connect('npc.db')
		self.memoryConnection = sqlite.connect(':memory:')
		self.cursor = self.connection.cursor()

	def addMounster(self):
		name = raw_input("Mounster's name: ")
		hp = raw_input("Mounster's Hitpoint: ")
		defance = raw_input("Mounster's Defance: ")
		attack = raw_input("Mounster's Attack: ")
		level = raw_input("Mounster's Level: ")
		exp = raw_input("Mounster's Exp: ")
		mdrop = raw_input("Mounster's Drop: ")

		self.cursor.execute('INSERT INTO npc VALUES (null, ?, ?, ?, ?, ?, ?, ?)', (name, mdrop, hp, defance, attack, level, exp))
		self.connection.commit()
		print "mounster %s is added" % name
		print "if you want add more just type A"
		keep = raw_input("Type: ")
		A = "A"
		if keep == A:
			return self.addMounster()
		else:
			sys.exit()

	#this creates npc.db file.
	def npcDB(self):
		self.cursor.execute('CREATE TABLE npc (id INTEGER PRIMARY KEY, name VARCHAR(30), mdrop VARCHAR(30), hp INTEGER, defance INTEGER, attack INTEGER, level INTEGER, exp INTEGER)')
		self.connection.commit()
		print "Tables created"
		print "if you want add mounsters just type A"
		keep = raw_input("Type: ")
		A = "A"
		if keep == A:
			return self.addMounster()
		else:
			sys.exit()

	#to view mounsters here we are.
	def viewMounster(self):
		self.cursor.execute('SELECT * FROM npc')      
		print self.cursor.fetchall()

	#update mounster's details
	def updateMounster(self):
		print "To update a Mounster you have to write its name"
		mname = raw_input("Mounster's name: ")
	
		self.cursor.execute('SELECT name FROM npc WHERE name LIKE ?', (mname,))
		row = self.cursor.fetchone()
		print "You selected", row[0]
		print "Write new values of", row[0]
		hp = raw_input("Mounster's Hitpoint: ")
		defance = raw_input("Mounster's Defance: ")
		attack = raw_input("Mounster's Attack: ")
		level = raw_input("Mounster's Level: ")
		exp = raw_input("Mounster's Exp: ")
		mdrop = raw_input("Mounster's Drop: ")

		self.cursor.execute('UPDATE npc SET hp=?, defance=?, resist=?, level=?, exp=?, mdrop=? WHERE name=? ',(hp,defance,attack,level,exp,mdrop,mname))
		self.connection.commit()
		print "Values updated"

gm_master = gm_master()