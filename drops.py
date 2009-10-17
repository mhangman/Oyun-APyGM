# -*- coding: utf-8 -*-
from pysqlite2 import dbapi2 as sqlite

#here we create drops at the db
def createDrops():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	print "Please write what drops you want"
	drop = raw_input("Drop: ")
	cursor.execute('INSERT INTO STASH VALUES (null, ?, 0)', (drop,))
	connection.commit()
	return createDrops()

print "creating drop list"
createDrops()