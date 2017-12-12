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
import MainAdminUI as maui


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
        self.btnExit = QPushButton("Exit", self)
        self.btnProblem.setMinimumHeight(40)
        self.btnProblem.setStyleSheet('margin-left: 80px;margin-right:80px;')
        self.btnAdmin.setMinimumHeight(40)
        self.btnAdmin.setStyleSheet('margin-left: 80px;margin-right:80px;')
        self.btnExit.setMinimumHeight(40)
        self.btnExit.setStyleSheet('margin-left: 80px;margin-right:80px;')
        self.btnExit.clicked.connect(lambda : self.Exit())
        self.btnProblem.clicked.connect(lambda : self.toProblem())
        self.btnAdmin.clicked.connect(lambda : self.toAdmin())
    #the Layout of the Program
    def LayoutofP(self):
        # add on screen items
        self.layout = QGridLayout()
        self.layout.addWidget(self.btnProblem,0,0)
        self.layout.addWidget(self.btnAdmin,1,0)
        self.layout.addWidget(self.btnExit,2,0)
    #switching window
    def toAdmin(self):
        print "hello"
        ex = maui.StartMenu()
        ex.show()

    def toProblem(self):
        ex = mui.MainWindow()
        ex.show()
        self.close()

    #exit
    def Exit(self):
        QApplication.quit()
