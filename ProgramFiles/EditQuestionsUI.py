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
        #crete Questions list area
        self.makeQuesitonlist()
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


    def makeQuesitonlist(self):
        #make elemts for scroll box to work
        mygroupbox = QGroupBox("Difficulty, Question, Answer")
        myform = QFormLayout()
        labellist = []
        combolist = []
        buttonlist = []
        folder = "%s\Topics" % os.getcwd()
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                #does a file already exist with that difficulty?
                if filename.startswith("%s" % self.TopicName):
                    Found = True
                    print "nice"    
        """
        if Found == True:
            #read it
            linebline = []
            File = open("%s\%s_%d.txt" % (folder,self.TopicName, diff),'r')
            FileR = File.read()
            Questions = FileR.split("\n")
            for question in Questions:
                linebline.append(question.split(","))
            File.close()
            linebline.append(line)
            #Write to it
            File = open("%s\%s_%d.txt" % (folder,self.TopicName, diff),'w')
            for _ in range(0,len(linebline)):
                if _ != len(linebline) - 1:
                    File.write("%s,%s,%s\n" % (linebline[_][0],linebline[_][1],linebline[_][2]))
                else:
                    File.write("%s,%s,%s" % (linebline[_][0],linebline[_][1],linebline[_][2]))
        """
        for i in range(5):
            diff = i
            text = "1 + %d" % i
            answer = 1 + i
            labellist.append(QLabel('%d, what is the soluction this %s, %d' % (diff, text,answer)))
            combolist.append(QPushButton("Edit"))
            buttonlist.append(QPushButton("Delete"))
            hbox = QHBoxLayout()
            hbox.addWidget(combolist[i])
            hbox.addWidget(buttonlist[i])
            myform.addRow(labellist[i],hbox)
        mygroupbox.setLayout(myform)
        self.scroll = QScrollArea()
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
