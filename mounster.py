#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pysqlite2 import dbapi2 as sqlite

def addMounster():
	connection = sqlite.connect('npc.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor() 
	
	cursor.execute('CREATE TABLE npc (id INTEGER PRIMARY KEY, name VARCHAR(30), hp INTEGER, defance INTEGER, resist INTEGER, level INTEGER, exp INTEGER)')

	name = raw_input("Mounster's name: ")
	hp = raw_input("Mounster's Hitpoint: ")
	defance = raw_input("Mounster's Defance: ")
	resist = raw_input("Mounster's Resist: ")
	level = raw_input("Mounster's Level: ")
	exp = raw_input("Mounster's Exp: ")


	cursor.execute('INSERT INTO npc VALUES (null, ?, ?, ?, ?, ?, ?)', (name, hp, defance, resist, level, exp))
	connection.commit()