
"""
Author: Marcus Facchino
Description:
    The UI of the Edit Topic Window
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

SubjectsDic = {}
for subject in subjects:
    listt = []
    topic = subject.split(",")[0]
    topicDiff = subject.split(",")[1:-1]
    SubjectsDic[topic] = topic, topicDiff


class MainWindow(QMainWindow):
    #init
    def __init__(self, TopicName):
        super(MainWindow, self).__init__()
        self.TopicName = TopicName
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Edit Topic menu page')
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
        self.lbl_TopicN = QLabel("%s" % self.TopicName)
        self.lbl_TopicChange = QLabel("Change Topic Name:")
        self.lbl_TopicDChange = QLabel("Add or Remove Topic Difficulties:")
        self._TopicName = QLineEdit()
        self._TopicName.setMaxLength(20)
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.chb_diff1 = QCheckBox("7",self)
        self.chb_diff2 = QCheckBox("8",self)
        self.chb_diff3 = QCheckBox("9",self)
        self.chb_diff4 = QCheckBox("10",self)
        self.chb_diff5 = QCheckBox("11",self)
        self.chb_diff6 = QCheckBox("12",self)
        self.lbl_TopicN.setFixedHeight(50)
        self.btnExit = QPushButton("Exit", self)
        self.btnConfirm = QPushButton("Confirm", self)
        self.btnDelete = QPushButton("Delete!", self)
        self.btnExit.setMinimumHeight(30)
        self.btnConfirm.setMinimumHeight(30)
        self.btnDelete.setMinimumHeight(30)
        self.btnExit.clicked.connect(lambda: self.toMenu())
        self.btnConfirm.clicked.connect(lambda: self.confirm())
        self.btnDelete.clicked.connect(lambda: self.Delete())


    def LayoutofP(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.lbl_TopicN,0,0,1,7)
        self.layout.addWidget(self.lbl_TopicChange,1,0)
        self.layout.addWidget(self._TopicName,1,1,1,4)
        self.layout.addWidget(self.lbl_TopicDChange,2,0)
        self.layout.addWidget(self.chb_diff1,2,1)
        self.layout.addWidget(self.chb_diff2,2,2)
        self.layout.addWidget(self.chb_diff3,2,3)
        self.layout.addWidget(self.chb_diff4,2,4)
        self.layout.addWidget(self.chb_diff5,2,5)
        self.layout.addWidget(self.chb_diff6,2,6)
        self.layout.addWidget(self.btnDelete,3,0)
        self.layout.addWidget(self.btnConfirm,3,1,1,3)
        self.layout.addWidget(self.btnExit,3,4,1,3)

    def confirm(self):
        #checks if name field has input
        name = False
        prev = " "
        for num in str(self._TopicName.text()):
            if num == prev and num == " ":
                print "enter a valid name"
                break
            else:
                prev = num
                print "good"

    def Delete(self):
        if self.TopicName in SubjectsDic:
            print "%s" % SubjectsDic[self.TopicName][0]
        else:
            print "uh oh"

    def toMenu(self):
        ex = menui.StartMenu()
        ex.show()
        self.close()
