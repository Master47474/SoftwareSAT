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
import MainAdminUI as maui
import MainUI as mui

#variables

#The main class
class StartMenu(QMainWindow):
    #init functipm
    def __init__(self):
        super(StartMenu, self).__init__()
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Start menu page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(400,300)
        #creation of all elements
        self.createBtns()
        #laying out all elements
        self.LayoutofP()

        #Modifying the widget so that is can have extra fetures
        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)

    #Center the Window on screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        #moving the window to center
        self.move(qr.topLeft())

    #creating the Elements for the UI
    def createBtns(self):
        #elements
        self.btnProblem = QPushButton("Problems", self)
        self.btnAdmin = QPushButton("Admin", self)
        self.btnExit = QPushButton("Exit", self)
        #Adjectments to looks
        self.btnProblem.setMinimumHeight(40)
        self.btnAdmin.setMinimumHeight(40)
        self.btnExit.setMinimumHeight(40)
        self.btnProblem.setStyleSheet('margin-left: 80px;margin-right:80px;')
        self.btnAdmin.setStyleSheet('margin-left: 80px;margin-right:80px;')
        self.btnExit.setStyleSheet('margin-left: 80px;margin-right:80px;')
        #on clicked events
        self.btnExit.clicked.connect(lambda : self.Exit())
        self.btnProblem.clicked.connect(lambda : self.toProblem())
        self.btnAdmin.clicked.connect(lambda : self.toAdmin())

    #the Layout of the elemetns
    def LayoutofP(self):
        # add on screen items
        self.layout = QGridLayout()
        self.layout.addWidget(self.btnProblem,0,0)
        self.layout.addWidget(self.btnAdmin,1,0)
        self.layout.addWidget(self.btnExit,2,0)

    #switching windows
    #to Admin Window
    def toAdmin(self):
        global ex
        ex = maui.MainAWindow()
        ex.show()
        self.close()
    #to Problem Window
    def toProblem(self):
        global ex
        ex = mui.MainWindow()
        ex.show()
        self.close()
    #Exit the application
    def Exit(self):
        QApplication.quit()
