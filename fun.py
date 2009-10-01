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

	if toplam == 20:
		print "stats are ok"
		canavarlar = {"kutupayisi":"50","demon":"30","bildircin":"20","solucan":"5"}
		sans = random.choice(canavarlar.keys())
		canavar = canavarlar[sans]
		sal = 2
		saglik = row[2] * 5
		attack = row[4]

		print "first fight begins..."
		if saglik == 0:
			print "Gratz! You are dead before you start the game, zero hp!"
		else:
			while saglik > 0:
				saglik = int(saglik) - int(sal)
				print "your life is down to %s" % saglik
				canavar = int(canavar) - int(attack)
				print "mounster's life is %s" % canavar
				if canavar == 0:
					print "you win ohh yeahhh"
					break
				elif canavar<int(attack):
					canavar = 0
					print "canavarın canı %s'e indi" % canavar
					print "you win ohh yeahhh"
					break
				elif saglik == 0:
					print "so dead is only truth you have"
					break
				else:
					continue

	else:
		print "stats total must be 20."
	return run()