#!/usr/bin/env python
# -*- coding: utf-8 -*-
# APyGM (Another Python Game)
#
# Copyright (C) Ceyhun Alyeþil 2009 <ceyhunalyesil@gmail.com>
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
from PyQt4 import QtCore, QtGui

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
	cursor.execute('CREATE TABLE stash (id INTEGER PRIMARY KEY, name VARCHAR(30), number INTEGER)')
	cursor.execute('CREATE TABLE gold (id INTEGER PRIMARY KEY, goldhave INTEGER)')
	
	class Ui_MainWindow(object):
		def setupUi(self, MainWindow):
			MainWindow.setObjectName("MainWindow")
			MainWindow.resize(279, 235)
			self.centralwidget = QtGui.QWidget(MainWindow)
			self.centralwidget.setObjectName("centralwidget")
			self.lineEdit = QtGui.QLineEdit(self.centralwidget)
			self.lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 20))
			self.lineEdit.setObjectName("lineEdit")
			self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
			self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 113, 20))
			self.lineEdit_2.setObjectName("lineEdit_2")
			self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
			self.lineEdit_3.setGeometry(QtCore.QRect(120, 80, 113, 20))
			self.lineEdit_3.setObjectName("lineEdit_3")
			self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
			self.lineEdit_4.setGeometry(QtCore.QRect(120, 100, 113, 20))
			self.lineEdit_4.setObjectName("lineEdit_4")
			self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
			self.lineEdit_5.setGeometry(QtCore.QRect(120, 140, 113, 20))
			self.lineEdit_5.setObjectName("lineEdit_5")
			self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
			self.lineEdit_6.setGeometry(QtCore.QRect(120, 120, 113, 20))
			self.lineEdit_6.setObjectName("lineEdit_6")
			self.label = QtGui.QLabel(self.centralwidget)
			self.label.setGeometry(QtCore.QRect(10, 10, 241, 21))
			self.label.setObjectName("label")
			self.label_2 = QtGui.QLabel(self.centralwidget)
			self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 16))
			self.label_2.setObjectName("label_2")
			self.label_3 = QtGui.QLabel(self.centralwidget)
			self.label_3.setGeometry(QtCore.QRect(10, 60, 51, 16))
			self.label_3.setObjectName("label_3")
			self.label_4 = QtGui.QLabel(self.centralwidget)
			self.label_4.setGeometry(QtCore.QRect(10, 80, 46, 14))
			self.label_4.setObjectName("label_4")
			self.label_5 = QtGui.QLabel(self.centralwidget)
			self.label_5.setGeometry(QtCore.QRect(10, 100, 46, 14))
			self.label_5.setObjectName("label_5")
			self.label_6 = QtGui.QLabel(self.centralwidget)
			self.label_6.setGeometry(QtCore.QRect(10, 120, 61, 16))
			self.label_6.setObjectName("label_6")
			self.label_7 = QtGui.QLabel(self.centralwidget)
			self.label_7.setGeometry(QtCore.QRect(10, 140, 101, 16))
			self.label_7.setObjectName("label_7")
			self.pushButton = QtGui.QPushButton(self.centralwidget)
			self.pushButton.setGeometry(QtCore.QRect(140, 170, 75, 24))
			self.pushButton.setObjectName("pushButton")
			MainWindow.setCentralWidget(self.centralwidget)
			self.menubar = QtGui.QMenuBar(MainWindow)
			self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 19))
			self.menubar.setObjectName("menubar")
			self.menuMenu = QtGui.QMenu(self.menubar)
			self.menuMenu.setObjectName("menuMenu")
			MainWindow.setMenuBar(self.menubar)
			self.statusbar = QtGui.QStatusBar(MainWindow)
			self.statusbar.setObjectName("statusbar")
			MainWindow.setStatusBar(self.statusbar)
			self.actionAbout = QtGui.QAction(MainWindow)
			self.actionAbout.setObjectName("actionAbout")
			self.actionHelp = QtGui.QAction(MainWindow)
			self.actionHelp.setObjectName("actionHelp")
			self.actionExit = QtGui.QAction(MainWindow)
			self.actionExit.setObjectName("actionExit")
			self.menuMenu.addAction(self.actionAbout)
			self.menuMenu.addAction(self.actionHelp)
			self.menuMenu.addAction(self.actionExit)
			self.menubar.addAction(self.menuMenu.menuAction())

			self.retranslateUi(MainWindow)
			QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
			QtCore.QMetaObject.connectSlotsByName(MainWindow)

		def retranslateUi(self, MainWindow):
			MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "APyGM", None, QtGui.QApplication.UnicodeUTF8))
			self.label.setText(QtGui.QApplication.translate("MainWindow", "Welcome to APyGM please enter your stats:", None, QtGui.QApplication.UnicodeUTF8))
			self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Your name:", None, QtGui.QApplication.UnicodeUTF8))
			self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Hitpoint:", None, QtGui.QApplication.UnicodeUTF8))
			self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Power:", None, QtGui.QApplication.UnicodeUTF8))
			self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Dex:", None, QtGui.QApplication.UnicodeUTF8))
			self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Charisma:", None, QtGui.QApplication.UnicodeUTF8))
			self.label_7.setText(QtGui.QApplication.translate("MainWindow", "How smart you are? :", None, QtGui.QApplication.UnicodeUTF8))
			self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
			self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
			self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
			self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
			self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
	
	heroname = self.lineEdit.text()
	hp = self.lineEdit_2.text()
	intel = self.lineEdit_6.text()
	power = self.lineEdit_3.text()
	charisma = self.lineEdit_5.text()
	dex = self.lineEdit_4.text()
	
	#start to insert first values
	cursor.execute('INSERT INTO karakterler VALUES (null, ?, ?, ?, ?, ?, ?)', (heroname, hp, intel, power, charisma, dex))
	cursor.execute('INSERT INTO gain VALUES (null, 1)')
	cursor.execute('INSERT INTO lvl VALUES (null, 1)')
	cursor.execute('INSERT INTO gold VALUES (null, 0)')
	connection.commit()

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())

game_basic.run()