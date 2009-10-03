#!/usr/bin/env python
# -*- coding: utf-8 -*-
#APyGM coding by ceyhun alyeşil(ceyhunalyesil@gmail.com)

from pysqlite2 import dbapi2 as sqlite
from fun import *
from grind import *

try:
  dosya = open("test.db", "r")
except:
  print "Soon character creation will start you stats must be total 30 points no more "
  connection = sqlite.connect('test.db')
  memoryConnection = sqlite.connect(':memory:')
  cursor = connection.cursor() 

  cursor.execute('CREATE TABLE karakterler (id INTEGER PRIMARY KEY, isim VARCHAR(30), can INTEGER, intel INTEGER, power INTEGER, charisma INTEGER, dex INTEGER)')  
  cursor.execute('CREATE TABLE gain (id INTEGER PRIMARY KEY, exp INTEGER)')

  karakter = raw_input("Your name: ")
  can = raw_input("Your HP: ")
  intel = raw_input("How smart you are: ")
  power = raw_input("Str: ")
  charisma = raw_input("Charisma: ")
  dex = raw_input("Dex: ")

  cursor.execute('INSERT INTO karakterler VALUES (null, ?, ?, ?, ?, ?, ?)', (karakter, can, intel, power, charisma, dex))
  cursor.execute('INSERT INTO gain VALUES (null, 1)')
  connection.commit()


run()
