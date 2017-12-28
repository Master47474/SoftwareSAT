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
        #cosmetic effects fo Ui elements1
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.lbl_TopicN.setFixedHeight(50)
        #assign buttons
        self.btnApplyFilter.clicked.connect(lambda: self.makeQuesitonlist())
        #crete Questions list area
        self.makeQuesitonlist()


    def makeQuesitonlist(self):
        #make elemts for scroll box to work
        #was the filter changed?
        try:
            self.scroll.deleteLater()
            self.scroll = QScrollArea()
            self.layout.addWidget(self.scroll,4,0,4,12)
        except:
            self.scroll = QScrollArea()
        #get the filters
        self.filter = []
        for cbh in self.chbList:
            if cbh.isChecked() == True:
                self.filter.append(int(cbh.text()))
        #ui cosmetics
        mygroupbox = QGroupBox("Difficulty, Question, Answer")
        myform = QFormLayout()
        files = []
        folder = "%s\Topics" % os.getcwd()
        #are there any files for this topic?
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                #does a file already exist with that difficulty?
                if filename.startswith("%s" % self.TopicName):
                    Found = True
                    files.append(filename)
        #was at least one found?
        if Found == True:
            #init the line no.
            line = 1
            for filename in files:
                #read the file and get the questions
                linebline = []
                File = open("%s\%s" % (folder, filename),'r')
                FileR = File.read()
                Questions = FileR.split("\n")
                #for each question, get the diff,text,answer and append and make it a row
                for question in Questions:
                    linebline.append(question.split(","))
                    for _ in range(0,len(linebline)):
                        try:
                            diff = int(filename[11:13])
                        except:
                            diff = int(filename[11])
                        if diff in self.filter:
                            print self.filter
                            print diff
                            if len(linebline[_][0]) > 20:
                                linebline[_][0] = "%s..." % linebline[_][0][0:20]
                            if len(linebline[_][1]) > 15:
                                linebline[_][1] = "%s..." % linebline[_][1][0:15]
                            text = linebline[_][0]
                            answer = linebline[_][1]
                            hbox = QHBoxLayout()
                            hbox.addWidget(QPushButton("Edit"))
                            hbox.addWidget(QPushButton("Delete"))
                            myform.addRow(QLabel('%d, %s, %s' % (diff,text,answer)),hbox)
                            line += 1
        mygroupbox.setLayout(myform)
        self.scroll.setWidget(mygroupbox)

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
        self.layout.addWidget(self.scroll,4,0,4,12)
