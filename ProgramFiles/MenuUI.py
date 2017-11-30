"""
Author: Marcus Facchino
Description:
    The UI of the Start menu Window
"""
#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#File Imports
import MainUI as mui


class StartMenu(QMainWindow):
    #init
    def __init__(self):
        super(StartMenu, self).__init__()
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Start menu page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(400,300)
        self.createBtns()
        self.LayoutofP()

        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #crete the butttons for navigation
    def createBtns(self):
        self.btnProblem = QPushButton("Problems", self)
        self.btnAdmin = QPushButton("Admin", self)
        self.btnProblem.setMinimumHeight(40)
        self.btnProblem.setStyleSheet('margin-left: 60px;margin-right:30px;')
        self.btnAdmin.setMinimumHeight(40)
        self.btnAdmin.setStyleSheet('margin-left: 30px;margin-right:60px;')
        self.btnProblem.clicked.connect(lambda : self.toProblem())
        self.btnProblem.clicked.connect(lambda : self.toAdmin())
    #the Layout of the Program
    def LayoutofP(self):
        # add on screen items
        self.layout = QGridLayout()
        self.layout.addWidget(self.btnProblem,0,0)
        self.layout.addWidget(self.btnAdmin,0,2)
    #switching window
    def toProblem(self):
        ex = mui.MainWindow()
        ex.show()
        self.close()
    def toAdmin(self):
        print "to admin"
