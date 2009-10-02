#!/usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by ceyhun alyeşil(ceyhunalyesil@gmail.com)

from pysqlite2 import dbapi2 as sqlite
from fun import *

def ctable():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor() 

	cursor.execute('CREATE TABLE gain (id INTEGER PRIMARY KEY, exp INTEGER, lvl INTEGER)')
	connection.commit()

def gexp():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor() 

	expget = mexp
	cursor.execute('INSERT INTO gain VALUES (null, ?)', (expget))
	connection.commit()
