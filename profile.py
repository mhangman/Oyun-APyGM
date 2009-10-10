#!/usr/bin/env python
# -*- coding: utf-8 -*-
# APyGM (Another Python Game)
# 
# Copyright (C) Ceyhun Alyeşil 2009 <ceyhunalyesil@gmail.com>
# Open with GPLv3

from pysqlite2 import dbapi2 as sqlite

class sProfile:
	def __init__(self):
		connection = sqlite.connect('test.db')
		memoryConnection = sqlite.connect(':memory:')
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM karakterler')
		row = cursor.fetchone()

		self.hp = row[2]
		self.intel = row[3]
		self.power = row[4]
		self.charisma = row[5]
		self.dex = row[6]

	def viewStats(self):
		print "HP:", self.hp
		print "INT:", self.intel
		print "STR:", self.power
		print "CHA:", self.charisma
		print "DEX:", self.dex

sProfile = sProfile()