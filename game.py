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

from pysqlite2 import dbapi2 as sqlite
from fun import *

try:
  dosya = open("test.db", "r")
except:
  print "Soon character creation will start, your stats must be total 30 points. no more "
  connection = sqlite.connect('test.db')
  memoryConnection = sqlite.connect(':memory:')
  cursor = connection.cursor() 

#start to create tables
  cursor.execute('CREATE TABLE karakterler (id INTEGER PRIMARY KEY, isim VARCHAR(30), can INTEGER, intel INTEGER, power INTEGER, charisma INTEGER, dex INTEGER)')  
  cursor.execute('CREATE TABLE gain (id INTEGER PRIMARY KEY, exp INTEGER)')
  cursor.execute('CREATE TABLE lvl (id INTEGER PRIMARY KEY, number INTEGER)')

  heroname = raw_input("Your name: ")
  hp = raw_input("Your HP: ")
  intel = raw_input("How smart you are: ")
  power = raw_input("Str: ")
  charisma = raw_input("Charisma: ")
  dex = raw_input("Dex: ")

  #start to insert first values
  cursor.execute('INSERT INTO karakterler VALUES (null, ?, ?, ?, ?, ?, ?)', (heroname, hp, intel, power, charisma, dex))
  cursor.execute('INSERT INTO gain VALUES (null, 1)')
  cursor.execute('INSERT INTO lvl VALUES (null, 1)')
  connection.commit()

run()
