"""
Author: Marcus Facchino
Description:
    The UI of the Main Admin Window
"""
#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#File Imports
import MenuUI as menui

File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")


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
    #the Layout of the Program
    def LayoutofP(self):
        # add on screen items
        self.layout = QGridLayout()
        self.layout.addWidget(self.btnProblem,0,0)
        self.layout.addWidget(self.btnAdmin,1,0)
        self.layout.addWidget(self.btnExit,2,0)



"""
class MainWindow(QMainWindow):
    #init
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Admin menu page')
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
    def createBtns(self):
        self.lbl_Diff = QLabel("Difficulty :")
        self.cbx_topics = QComboBox(self)
        self.cbx_topics.addItem("7")
        self.cbx_topics.addItem("8")
        #for subject in subjects:
            #self.cbx_topics.addItem(str(subject.split(",")[0]))
    def LayoutofP(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.cbx_topics,0,0)
        self.layout.addWidget(self.lbl_Diff,0,1)
"""
