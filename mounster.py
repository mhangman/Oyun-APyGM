#!/usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by Ceyhun Alyeşil (ceyhunalyesil@gmail.com)
#license:gplv3

from pysqlite2 import dbapi2 as sqlite
import sys

#this for adding mounsters
def addMounster():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	name = raw_input("Mounster's name: ")
	hp = raw_input("Mounster's Hitpoint: ")
	defance = raw_input("Mounster's Defance: ")
	attack = raw_input("Mounster's Attack: ")
	level = raw_input("Mounster's Level: ")
	exp = raw_input("Mounster's Exp: ")
	drop = raw_input("Mounster's Drop: ")


	cursor.execute('INSERT INTO npc VALUES (null, ?, ?, ?, ?, ?, ?, ?)', (name, hp, defance, attack, level, exp, drop))
	connection.commit()
	print "mounster %s is added" % name
	print "if you want add more just type A"
	keep = raw_input("Type: ")
	A = "A"
	if keep == A:
		return addMounster()
	else:
		sys.exit()

#this creates npc.db file.
def npcDB():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor() 
	
	cursor.execute('CREATE TABLE npc (id INTEGER PRIMARY KEY, name VARCHAR(30), hp INTEGER, defance INTEGER, resist INTEGER, level INTEGER, exp INTEGER, drop VARCHAR(30))')

	connection.commit()
	print "Tables created"
	print "if you want add mounsters just type A"
	keep = raw_input("Type: ")
	A = "A"
	if keep == A:
		return addMounster()
	else:
		sys.exit()

#to view mounsters here we are.
def viewMounster():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM npc')
      
	print cursor.fetchall()

#update mounster's details
def updateMounster():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	print "To update a Mounster you have to write its name"
	mname = raw_input("Mounster's name: ")
	
	cursor.execute('SELECT name FROM npc WHERE name LIKE ?', (mname,))
	row = cursor.fetchone()
	print "You selected", row[0]
	print "Write new values of", row[0]
	hp = raw_input("Mounster's Hitpoint: ")
	defance = raw_input("Mounster's Defance: ")
	attack = raw_input("Mounster's Attack: ")
	level = raw_input("Mounster's Level: ")
	exp = raw_input("Mounster's Exp: ")
	drop = raw_input("Mounster's Drop: ")

	cursor.execute('UPDATE npc SET hp=?, defance=?, resist=?, level=?, exp=?, drop=? WHERE name=? ',(hp,defance,attack,level,exp,drop,mname))
	connection.commit()
	print "Values updated"

	