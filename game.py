#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding by ceyhun alyeşil(ceyhunalyesil@gmail.com)

from pysqlite2 import dbapi2 as sqlite
from fun import *

try:
  dosya = open("test.db", "r")
except:
  print "Soon character creation will start you stats must be total 20 points no more "
  connection = sqlite.connect('test.db')
  memoryConnection = sqlite.connect(':memory:')
  cursor = connection.cursor() 

  cursor.execute('CREATE TABLE karakterler (id INTEGER PRIMARY KEY, isim VARCHAR(30), can INTEGER, intel INTEGER, power INTEGER, charisma INTEGER, dex INTEGER)')

  karakter = raw_input("isminiz: ")
  can = raw_input("can degerini girin: ")
  intel = raw_input("Zeka puanı: ")
  power = raw_input("Güç puanı: ")
  charisma = raw_input("Karizma puanı: ")
  dex = raw_input("Çeviklik puanı: ")

  cursor.execute('INSERT INTO karakterler VALUES (null, ?, ?, ?, ?, ?, ?)', (karakter, can, intel, power, charisma, dex))
  connection.commit()

run()
