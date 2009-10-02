#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding by ceyhun alyeşil(ceyhunalyesil@gmail.com)

import sys
import random
from pysqlite2 import dbapi2 as sqlite

def run():
	while True:
		print "Hello young one. We are happy to see you here. I wish to say that some time we had peace."
		print "but the truth is we never had. if you want to change something in the world choose"
		print "your direction. To fight write S to quit just write Q ." 
		komut = raw_input("Chicken or a warrior: ")
		veri = str(komut)
		S = "S"
		Q = "Q"
		if veri == S:
			fight()
		elif veri == Q:
			sys.exit()


def fight():
	connection = sqlite.connect('test.db')
	memoryConnection = sqlite.connect(':memory:')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM karakterler')
	row = cursor.fetchone()
	toplam = row[2]+row[3]+row[4]+row[5]+row[6]

	if toplam == 30:
		print "stats are ok"
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
						break
					elif mlife<int(pdamage):
						mlife = 0
						print "mounster's life is  %s" % mlife
						print "you win ohh yeahhh"
						break
					elif saglik == 0:
						print "so dead is only truth you have"
						break
					else:
						continue