#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding by ceyhun alyeşil(ceyhunalyesil@gmail.com)
#published with gplv3
import sys
import random
from pysqlite2 import dbapi2 as sqlite

def run():
	while True:
		print "Merhaba genç savaşçı, aramıza katılmana sevindik. Burası eskiden güzel bir yerdi demek isterdim."
		print "ama gerçek şu ki hiç bir zaman barış içinde olamadık. Madem artık bir şeyleri değiştirmek için sende"
		print "harekete geçtin.Savaşmak için S çıkmak için Q yazabilirsin." 
		komut = raw_input("Söyle bakalım ne istersin: ")
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
		print "işlem başarılı."
		canavarlar = {"kutupayisi":"50","demon":"30","bildircin":"20","solucan":"5"}
		sans = random.choice(canavarlar.keys())
		canavar = canavarlar[sans]
		sal = 2
		saglik = row[2] * 5
		attack = row[4]

		print "deneme savaşı başlatılıyor..."
		if saglik == 0:
			print "Tebrikler başlamadan kaybettiniz"
		else:
			while saglik > 0:
				saglik = int(saglik) - int(sal)
				print "canınız %s'e indi" % saglik
				canavar = int(canavar) - int(attack)
				print "canavarın canı %s'e indi" % canavar
				if canavar == 0:
					print "kazandınız ohh yeahhh"
					break
				elif canavar<int(attack):
					canavar = 0
					print "canavarın canı %s'e indi" % canavar
					print "kazandınız ohh yeahhh"
					break
				elif saglik == 0:
					print "öldünüz ühühü"
					break
				else:
					continue

	else:
		print "işlem başarısız."
	return run()