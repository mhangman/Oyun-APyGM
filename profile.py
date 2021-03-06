#!/usr/bin/env python
# -*- coding: utf-8 -*-
# APyGM (Another Python Game)
# 
# Copyright (C) Ceyhun Alyeşil 2009 <ceyhunalyesil@gmail.com>
# Open with GPLv3

from pysqlite2 import dbapi2 as sqlite

class sProfile:
	def __init__(self):
		self.connection = sqlite.connect('test.db')
		self.memoryConnection = sqlite.connect(':memory:')
		self.cursor = self.connection.cursor()

	def viewStats(self):
		self.cursor.execute('SELECT * FROM karakterler')
		row = self.cursor.fetchone()

		self.hp = row[2]
		self.intel = row[3]
		self.power = row[4]
		self.charisma = row[5]
		self.dex = row[6]
		print "HP:", self.hp
		print "INT:", self.intel
		print "STR:", self.power
		print "CHA:", self.charisma
		print "DEX:", self.dex

	def viewLevel(self):
		self.cursor.execute('SELECT * FROM lvl')
		lrow = self.cursor.fetchone()
		self.lvl = lrow[1]
		print "LEVEL:", self.lvl

	def viewExp(self):
		self.cursor.execute('SELECT * FROM gain')
		erow = self.cursor.fetchone()
		self.exp = erow[1]
		print "EXPERIENCE:", self.exp

	def viewStash(self):
		self.cursor.execute('SELECT * FROM stash')
		print self.cursor.fetchall()
#going to add armors here, player going to choose to wear them from profile windows

sProfile = sProfile()

