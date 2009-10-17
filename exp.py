# -*- coding: utf-8 -*-
import sys
import random
from pysqlite2 import dbapi2 as sqlite
from profile import *
from fun import *

class expsystem:
	def __init__(self):
		self.connection = sqlite.connect('test.db')
		self.memoryConnection = sqlite.connect(':memory:')
		self.cursor = self.connection.cursor()

	def gexp(self):
		self.cursor.execute('SELECT * FROM gain')
		expget = self.cursor.fetchone()
		exp = expget[1]
		from fun import arm
		cexp = exp + arm.mexp
		self.cursor.execute('UPDATE gain SET exp=?',(cexp,))
		self.connection.commit()
		self.cursor.execute('SELECT * FROM gain')
		cxpget = self.cursor.fetchone()
		pxp = cxpget[1]
		print "Your exp is %s" %pxp
		self.checkLevel()
 
	#lets loose exp when we die
	def lexp(self):
		self.cursor.execute('SELECT * FROM gain')
		exptake = self.cursor.fetchone()
		expnow = exptake[1]
		#have to test this
		explost = expnow * 2 / 100
		newexp = expnow - explost
		if newexp < 0:
			self.cursor.execute('UPDATE gain SET exp=0')
			self.connection.commit()
			print "Your exp is down to zero, good job"
		else:
			self.cursor.execute('UPDATE gain SET exp=?',(newexp,))
			self.connection.commit()
			self.cursor.execute('SELECT * FROM gain')
			nexp = self.cursor.fetchone()
			yourexp = nexp[1]
			print "Your exp is down to %s" %yourexp

	def checkLevel(self):
		self.cursor.execute('SELECT * FROM lvl')
		lvlget = self.cursor.fetchone()
		lvl = lvlget[1]

		elimit = lvl * 1000
		self.cursor.execute('SELECT * FROM gain')
		nexp = self.cursor.fetchone() 
		yourexp = nexp[1]

		if yourexp >= elimit:
			lvl = lvl + 1
			self.cursor.execute('UPDATE lvl SET number=?',(lvl,))
			self.connection.commit()
			print "Level up"
			self.cursor.execute('SELECT * FROM lvl')
			lvlget = self.cursor.fetchone()
			lvl = lvlget[1]
			print "Your level is:", lvl
			self.addToStats()

	#when we level up we will get +5 stats
	def addToStats(self):
		self.cursor.execute('SELECT * FROM karakterler')
		row = self.cursor.fetchone()
		hp = row[2] + 1
		intel = row[3] + 1 
		power = row[4] + 1 
		charisma = row[5] + 1
		dex = row[6] + 1

		self.cursor.execute('UPDATE karakterler SET can=?, intel=?, power=?, charisma=?, dex=?',(hp, intel, power, charisma, dex))
		self.connection.commit()

expsystem = expsystem()