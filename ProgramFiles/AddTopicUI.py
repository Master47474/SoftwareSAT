
"""
Author: Marcus Facchino
Description:
    The UI of the Add Topic Window
"""

#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import collections as col

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
        self.setWindowTitle('Testing UI For Add Topic menu page')
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
        self.lbl_TopicChange = QLabel("Topic Name:")
        self.lbl_TopicDChange = QLabel("Add Topic Difficulties:")
        self._TopicName = QLineEdit()
        self.btnExit = QPushButton("Exit", self)
        self.btnConfirm = QPushButton("Confirm", self)
        self.chb_diff1 = QCheckBox("7",self)
        self.chb_diff2 = QCheckBox("8",self)
        self.chb_diff3 = QCheckBox("9",self)
        self.chb_diff4 = QCheckBox("10",self)
        self.chb_diff5 = QCheckBox("11",self)
        self.chb_diff6 = QCheckBox("12",self)
        #list of all checkboxes
        cbx = [self.chb_diff1,self.chb_diff2,self.chb_diff3,self.chb_diff4,self.chb_diff5,self.chb_diff6]
        #should chekcbox start ticked?
        for num in range(0,len(cbx)):
            cbx[num].setChecked(True)
        #cosmetic effects fo Ui elements
        self._TopicName.setMaxLength(20)
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.lbl_TopicN.setFixedHeight(50)
        self.btnExit.setMinimumHeight(30)
        self.btnConfirm.setMinimumHeight(30)
        #on button clicked
        self.btnExit.clicked.connect(lambda: self.toMenu())
        self.btnConfirm.clicked.connect(lambda: self.confirm())

    #layout of Window
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
        self.layout.addWidget(self.btnConfirm,3,1,1,3)
        self.layout.addWidget(self.btnExit,3,4,1,3)

    #resplitting the Topics File
    def Splittting(self):
        File = open("Topics.txt",'r')
        FileR = File.read()
        subjects = FileR.split("\n")
        File.close()
        SubjectsDic = {}
        for subject in subjects:
            listt = []
            topic = subject.split(",")[0]
            topicDiff = subject.split(",")[1:]
            SubjectsDic[topic] = topic,topicDiff
        return SubjectsDic

    #Confirming the Changes
    def confirm(self):
        #reSplitting
        global SubjectsDic
        SubjectsDic = self.Splittting()
        cbx = [self.chb_diff1,self.chb_diff2,self.chb_diff3,self.chb_diff4,self.chb_diff5,self.chb_diff6]
        #checks if name field has input
        name = False
        prev = " "
        #me checking for doulbe spaces
        AllG = False
        for num in str(self._TopicName.text()):
            if num == prev and num == " ":
                print "enter a valid name"
                break
            else:
                AllG = True
            prev = num
        if AllG == True:
            #if the last letter is == to the last letter of the topic
            line = []
            line.append(str(self._TopicName.text()))
            for box in cbx:
                if box.isChecked():
                    line.append(int(box.text()))
                else:
                    line.append(0)
            print line
        File = File = open("Topics.txt",'a')
        File.write("\n%s,%d,%d,%d,%d,%d,%d" % (line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
        File.close()
        #self.toMenu()


    #To the Main Admin Menu
    def toMenu(self):
        ex = maui.MainAWindow(self.TopicName)
        ex.show()
        self.close()
