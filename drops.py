# -*- coding: utf-8 -*-
from pysqlite2 import dbapi2 as sqlite

#here we create drops at the db
def createDrops():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
	
	cursor.execute('INSERT INTO stash VALUES (null, wblood, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, crowfeather, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, spoison, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, tfur, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, bfur, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, gdust, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, fang, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, vdust, 0)')
	cursor.execute('INSERT INTO stash VALUES (null, soulgem, 0)')

	connection.commit()
