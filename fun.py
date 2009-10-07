#!/usr/bin/env python
# -*- coding: utf-8 -*-
# APyGM (Another Python Game)
# 
# Copyright (C) Ceyhun Alyeşil 2009 <ceyhunalyesil@gmail.com>
#
# APyGM is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# APyGM is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import random
from pysqlite2 import dbapi2 as sqlite

#starter function. 
def run():
	while True:
		print "Hello young one. We are happy to see you here. I wish to say that some time we had peace."
		print "but the truth is we never had. if you want to change something in the world choose"
		print "your direction. To fight write S to quit just write Q ." 
		order = raw_input("Chicken or a warrior: ")
		runorder = str(order)
		S = "S"
		Q = "Q"
		if runorder == S:
			fight()
		elif runorder == Q:
			sys.exit()


def fight():
	global mexp
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM karakterler')
	row = cursor.fetchone()
	toplam = row[2]+row[3]+row[4]+row[5]+row[6]

	if toplam >= 30:
		print "stats are ok for now..."
		saglik = row[2] * 5
		attack = row[4] * 2

		connection = sqlite.connect('npc.db')
		memoryConnection = sqlite.connect(':memory:')
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM npc ORDER BY RANDOM()')
		war = cursor.fetchone()

		mlife = war[2]
		mattack = war[4]
		mdefance = war[3]
		mexp = war[6]

		pdamage = int(attack) - int(mdefance)

		if int(mdefance) > int(attack):
			print "He is stronger than we thought... RUNNN!"
		else:
			print "first fight begins..."
			if saglik == 0:
				print "Gratz! You are dead before you start the game, zero hp!"
			else:
				while saglik > 0:
					saglik = int(saglik) - int(mattack)
					print "your life is down to %s" % saglik
					mlife = int(mlife) - int(pdamage)
					print "mounster's life is %s" % mlife
					if mlife == 0:
						print "you win ohh yeahhh"
						gexp()
						break
					elif mlife<int(pdamage):
						mlife = 0
						print "mounster's life is  %s" % mlife
						print "you win ohh yeahhh"
						gexp()
						break
					elif saglik == 0:
						print "so death is only truth you have"
						lexp()
						break
					else:
						continue
#exp getting
def gexp():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
 
	cursor.execute('SELECT * FROM gain')
	expget = cursor.fetchone()
	exp = expget[1]
 
	cexp = exp + mexp
	cursor.execute('UPDATE gain SET exp=?',(cexp,))
	connection.commit()
	cursor.execute('SELECT * FROM gain')
	cxpget = cursor.fetchone()
	pxp = cxpget[1]
	print "Your exp is %s" %pxp
	checkLevel()

#lets loose exp when we die
def lexp():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM gain')
	exptake = cursor.fetchone()
	expnow = exptake[1]
#have to test this
	explost = expnow * 2 / 100
	newexp = expnow - explost
	if newexp < 0:
		cursor.execute('UPDATE gain SET exp=0')
		cursor.commit()
		print "Your exp is down to zero, good job"
	else:
		cursor.execute('UPDATE gain SET exp=?',(newexp,))
		connection.commit()
		cursor.execute('SELECT * FROM gain')
		nexp = cursor.fetchone() 
		yourexp = nexp[1]
		print "Your exp is down to %s" %yourexp

#gain lvl
def checkLevel():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM lvl')
	lvlget = cursor.fetchone()
	lvl = lvlget[1]

	elimit = lvl * 1000
	cursor.execute('SELECT * FROM gain')
	nexp = cursor.fetchone() 
	yourexp = nexp[1]

	if yourexp >= elimit:
		lvl = lvl + 1
		cursor.execute('UPDATE lvl SET number=?',(lvl,))
		connection.commit()
		print "Level up"
		cursor.execute('SELECT * FROM lvl')
		lvlget = cursor.fetchone()
		lvl = lvlget[1]
		print "Your level is:", lvl
		addToStats()
	else:
		return run()

#when we level up we will get +5 stats
def addToStats():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM karakterler')
	row = cursor.fetchone()
	hp = row[2] + 1
	intel = row[3] + 1 
	power = row[4] + 1 
	charisma = row[5] + 1
	dex = row[6] + 1

	cursor.execute('UPDATE karakterler SET can=?, intel=?, power=?, charisma=?, dex=?',(hp, intel, power, charisma, dex))
	connection.commit()