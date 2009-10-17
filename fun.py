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
from profile import *
from exp import *

#starter function. 
class game_basic:
	def run(self):
		while True:
			print "Hello young one. We are happy to see you here. I wish to say that some time we had peace."
			print "but the truth is we never had. if you want to change something in the world choose"
			print "your direction. To fight write S to quit just write Q. To see your profile just type P" 
			order = raw_input("Your order: ")
			runorder = str(order)
			S = "S"
			Q = "Q"
			P = "P"
			if runorder == S:
				arm.fight()
			elif runorder == Q:
				sys.exit()
			elif runorder == P:
				sProfile.viewStats()
				sProfile.viewLevel()
				sProfile.viewExp()
				sProfile.viewStash()

game_basic=game_basic()

class arm:
	def __init__(self):
		self.connection = sqlite.connect('test.db')
		memoryConnection = sqlite.connect(':memory:')
		self.cursor = self.connection.cursor()

	def fight(self):
		self.cursor.execute('SELECT * FROM karakterler')
		row = self.cursor.fetchone()
		toplam = row[2]+row[3]+row[4]+row[5]+row[6]

		if toplam >= 30:
			print "stats are ok for now..."
			self.saglik = row[2] * 6
			self.attack = row[4] * 3

			connection = sqlite.connect('npc.db')
			memoryConnection = sqlite.connect(':memory:')
			cursor = connection.cursor()
			cursor.execute('SELECT * FROM npc ORDER BY RANDOM()')
			war = cursor.fetchone()

			self.mlife = war[3]
			self.mattack = war[5]
			self.mdefance = war[4]
			self.mexp = war[7]
			self.drop = war[2]

			pdamage = int(self.attack) - int(self.mdefance)

			if int(self.mdefance) > int(self.attack):
				print "He is stronger than we thought... RUNNN!"
			else:
				print "first fight begins..."
				if self.saglik == 0:
					print "Gratz! You are dead before you start the game, zero hp!"
				else:
					while self.saglik > 0:
						self.saglik = int(self.saglik) - int(self.mattack)
						print "your life is down to %s" % self.saglik
						self.mlife = int(self.mlife) - int(pdamage)
						print "mounster's life is %s" % self.mlife
						if self.mlife == 0:
							print "you win ohh yeahhh"
							expsystem.gexp()
							depo.addToStash()
							break
						elif self.mlife<int(pdamage):
							mlife = 0
							print "mounster's life is  %s" % self.mlife
							print "you win ohh yeahhh"
							expsystem.gexp()
							depo.addToStash()
							break
						elif self.saglik == 0:
							print "so death is only truth you have"
							expsystem.lexp()
							break
						else:
							continue
arm = arm()
#when we kill a mounster we will add its drop to our stash, this function not finished
class depo:
	def __init__(self):
		self.connection = sqlite.connect('test.db')
		memoryConnection = sqlite.connect(':memory:')
		self.cursor = self.connection.cursor()
	def addToStash(self):
		drop = str(arm.drop)
		self.cursor.execute('SELECT * FROM stash WHERE name LIKE ?', (drop,))
		row = self.cursor.fetchone()
		number = row[2]
		number = number +1 
		self.cursor.execute('UPDATE stash SET number=? WHERE name=?', (number,drop))
		self.connection.commit()
		print "You gained:", drop

depo = depo()