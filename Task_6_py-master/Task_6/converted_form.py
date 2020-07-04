# -*- coding: utf-8 -*-

from PyQt5 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,600)

        self.ToolsButton = QtWidgets.QPushButton()
        self.HelpButton = QtWidgets.QPushButton()
        self.gridLayoutWidget = QtWidgets.QGridLayout()
        self.Lvl_label = QtWidgets.QLabel()
        self.Up_Button = QtWidgets.QPushButton()
        self.Down_Button = QtWidgets.QPushButton()
        self.RestartButton = QtWidgets.QPushButton()
        self.mainMenu=QtWidgets.QMenuBar()
        self.fileMenu=self.mainMenu.addMenu("Game") 

        self.vbox=QtWidgets.QVBoxLayout()
        self.hbox1=QtWidgets.QHBoxLayout()
        self.vbox2=QtWidgets.QVBoxLayout()
        self.hbox2=QtWidgets.QHBoxLayout()

        self.hbox1.addWidget(self.mainMenu)
        #self.hbox1.addWidget(self.ToolsButton)
        #self.hbox1.addWidget(self.HelpButton)

        self.vbox2.addWidget(self.Up_Button)
        self.vbox2.addWidget(self.Down_Button)

        self.hbox2.addWidget(self.Lvl_label)
        self.hbox2.addLayout(self.vbox2)
        self.hbox2.addWidget(self.RestartButton)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.gridLayoutWidget)
        self.vbox.addLayout(self.hbox2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayout(self.vbox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Цифровой кузнечик"))
        self.ToolsButton.setText(_translate("MainWindow", "Tools"))
        self.HelpButton.setText(_translate("MainWindow", "Help"))
        self.Lvl_label.setText(_translate("MainWindow", "Level:"))
        self.Up_Button.setText(_translate("MainWindow", "UpLvl"))
        self.Down_Button.setText(_translate("MainWindow", "DownLvl"))
        self.RestartButton.setText(_translate("MainWindow", "Restart"))
