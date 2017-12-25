"""
Author: Marcus Facchino
Description:
    The UI of the Edit Questions Window
"""

#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#File Imports
import MainAdminUI as maui

#Variables
File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")
File.close()

#a Dictionary of all the Topics
SubjectsDic = {}
for subject in subjects:
    listt = []
    #the topic
    topic = subject.split(",")[0]
    #The Difficulites of the topic
    topicDiff = subject.split(",")[1:]
    SubjectsDic[topic] = topic,topicDiff


class MainWindow(QMainWindow):
    #init
    def __init__(self, TopicName):
        super(MainWindow, self).__init__()
        #setting the Topic name chosen at the Previous screen
        self.TopicName = TopicName
        self.initUI()

    #init UI
    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Edit Questions menu page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(400,300)
        #Created the Ui Elements
        self.createBtns()
        #layout of the program
        self.LayoutofP()

        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)

    #centers the application
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #creates the UI elements
    def createBtns(self):
        #init Ui Elemtents
        self.lbl_TopicN = QLabel("%s" % self.TopicName)
        self.lbl_filter = QLabel("Filters:")
        self.chb_diff1 = QCheckBox("7",self)
        self.chb_diff2 = QCheckBox("8",self)
        self.chb_diff3 = QCheckBox("9",self)
        self.chb_diff4 = QCheckBox("10",self)
        self.chb_diff5 = QCheckBox("11",self)
        self.chb_diff6 = QCheckBox("12",self)
        self.chbList = [self.chb_diff1,self.chb_diff2,self.chb_diff3,self.chb_diff4,self.chb_diff5,self.chb_diff6]
        for chb in self.chbList:
            chb.setChecked(True)
        self.btnApplyFilter = QPushButton("Apply Filter", self)
        self.lblQuestions = QLabel("Questions:")
        #make elemts for scroll box to work
        self.ScrollArea = QScrollArea()
        self.SAVertivalBox = QVBoxLayout()
        self.QuestionRowLayout = QHBoxLayout()
        self.layoutofQuestions()
        #cosmetic effects fo Ui elements1
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.lbl_TopicN.setFixedHeight(50)

    #makes the layout of all the questions
    def layoutofQuestions(self):
        #set layouts for each area
        self.ScrollArea.setLayout(self.SAVertivalBox)
        self.rowLayout = QGridLayout()
        for row in range(0,5):
            for col in range(0,5):
                diff = QLabel("%d" % row)
                question = QLabel("1 + %d" % row + col)
                answer = QLabel("%d" % col + row + 1)
                edit = QPushButton("Edit", self)
                Delete = QPushButton("delete", self)
                self.rowLayout.addWidget(diff,row,col)
                self.rowLayout.addWidget(question,row,col)
                self.rowLayout.addWidget(answer,row,col)
                self.rowLayout.addWidget(edit,row,col)
                self.rowLayout.addWidget(Delete,row,col)


    #layout of Window
    def LayoutofP(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.lbl_TopicN,0,0,1,12)
        self.layout.addWidget(self.lbl_filter,1,0)
        self.layout.addWidget(self.chb_diff1,1,1)
        self.layout.addWidget(self.chb_diff2,1,2)
        self.layout.addWidget(self.chb_diff3,1,3)
        self.layout.addWidget(self.chb_diff4,1,4)
        self.layout.addWidget(self.chb_diff5,1,5)
        self.layout.addWidget(self.chb_diff6,1,6)
        self.layout.addWidget(self.btnApplyFilter,2,6)
        self.layout.addWidget(self.lblQuestions,3,0)
        self.layout.addWidget(self.ScrollArea,4,0,4,12)
