#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pysqlite2 import dbapi2 as sqlite
import sys

def addMounster():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	name = raw_input("Mounster's name: ")
	hp = raw_input("Mounster's Hitpoint: ")
	defance = raw_input("Mounster's Defance: ")
	resist = raw_input("Mounster's Resist: ")
	level = raw_input("Mounster's Level: ")
	exp = raw_input("Mounster's Exp: ")


	cursor.execute('INSERT INTO npc VALUES (null, ?, ?, ?, ?, ?, ?)', (name, hp, defance, resist, level, exp))
	connection.commit()
	print "mounster %s is added" % name
	print "if you want add more just type A"
	keep = raw_input("Type: ")
	A = "A"
	if keep == A:
		return addMounster()
	else:
		sys.exit()
def npcDB():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor() 
	
	cursor.execute('CREATE TABLE npc (id INTEGER PRIMARY KEY, name VARCHAR(30), hp INTEGER, defance INTEGER, resist INTEGER, level INTEGER, exp INTEGER)')

	connection.commit()
	print "Tables created"
	print "if you want add mounsters just type A"
	keep = raw_input("Type: ")
	A = "A"
	if keep == A:
		return addMounster()
	else:
		sys.exit()

def viewMounster():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM npc')
      
	print cursor.fetchall()