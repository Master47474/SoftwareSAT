
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

class MainAWindow(QMainWindow):
    #init
    def __init__(self):
        super(MainAWindow, self).__init__()
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
        self.lbl_Diff = QLabel("select a topic:")
        self.cbx_topics = QComboBox(self)
        for subject in subjects:
            self.cbx_topics.addItem(str(subject.split(",")[0]))
        self.btn_EditT = QPushButton("Edit Topic",self)
        self.btn_EditQ = QPushButton("Edit Question",self)
        self.btn_AddQ = QPushButton("Add Question",self)
        self.lbl_Diff.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.btn_AddT = QPushButton("Add Topic",self)
        self.btnExit = QPushButton("Exit", self)
        self.btnExit.setMinimumHeight(40)
        self.btnExit.clicked.connect(lambda: self.toMenu())
    def LayoutofP(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.lbl_Diff,0,0)
        self.layout.addWidget(self.cbx_topics,0,1)
        self.layout.addWidget(self.btn_EditT,1,0)
        self.layout.addWidget(self.btn_EditQ,2,0)
        self.layout.addWidget(self.btn_AddQ,3,0)
        self.layout.addWidget(self.btn_AddT,1,2)
        self.layout.addWidget(self.btnExit,4,2)

    def toMenu(self):
        ex = menui.StartMenu()
        ex.show()
        self.close()
