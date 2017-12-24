
"""
Author: Marcus Facchino
Description:
    The UI of the ADD Question Window
"""

#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import shutil as sht
import re
import string

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
    topic = subject.split(",")[0]
    topicDiff = subject.split(",")[1:]
    SubjectsDic[topic] = topic,topicDiff


class MainWindow(QMainWindow):
    #init
    def __init__(self, Topicname):
        super(MainWindow, self).__init__()
        #Init Vars
        self.TopicName = Topicname
        self.ImageForQ = ["",""]
        self.NotationOn = False
        self.initUI()

    #init UI
    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Admin menu page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(400,300)
        #creation of UI elements
        self.createBtns()
        #laysout the program
        self.LayoutofP()

        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)

    #centers application
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #creation of UI Elements
    def createBtns(self):
        #creation of Ui Elements
        self.lbl_TopicN = QLabel("%s" % self.TopicName)
        self.lbl_Diff = QLabel("Difficulty:", self)
        self.lbl_prb = QLabel("Problem:", self)
        self.lbl_Answer = QLabel("Answer:", self)
        self._Answer = QLineEdit()
        self._Problem = QTextEdit()
        self.cbx_diff = QComboBox(self)
        self.btn_Submit = QPushButton("Submit", self)
        self.btn_Exit = QPushButton("Exit", self)
        self.btn_Problem = QPushButton("Notation")
        self.btnBrowse = QPushButton("Browse")
        self.btnCnlimage = QPushButton("No Image")
        self.lbl_Error = QLabel("",self)
        self.cbxGroup = QButtonGroup(self)
        self.chb_diff1 = QRadioButton("Problem",self)
        self.chb_diff2 = QRadioButton("Answer",self)
        self.chb_diff1.setChecked(True)
        self.cbxGroup.addButton(self.chb_diff1,0)
        self.cbxGroup.addButton(self.chb_diff2,1)

        #Cosmetic effects for Ui
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.lbl_TopicN.setFixedHeight(50)
        #populating Dropdown box
        self.cbx_diff.addItem("7")
        self.cbx_diff.addItem("8")
        self.cbx_diff.addItem("9")
        self.cbx_diff.addItem("10")
        self.cbx_diff.addItem("11")
        self.cbx_diff.addItem("12")
        #on button clicked
        self.btnBrowse.clicked.connect(lambda: self.singleBrowse())
        self.btnCnlimage.clicked.connect(lambda: self.resetImag())
        self.btn_Submit.clicked.connect(lambda: self.submit(int(self.cbx_diff.currentText()), str(self._Problem.toPlainText()), str(self._Answer.text())))
        self.btn_Exit.clicked.connect(lambda: self.toMenu())
        self.btn_Problem.clicked.connect(lambda: self.notation())

    # layout os program
    def LayoutofP(self):
        global layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.lbl_TopicN,0,0,1,7)
        self.layout.addWidget(self.lbl_Diff,1,0)
        self.layout.addWidget(self.cbx_diff,1,1)
        self.layout.addWidget(self.lbl_Error,1,5,1,2)
        self.layout.addWidget(self.lbl_prb,2,0)
        self.layout.addWidget(self._Problem,2,1,1,4)
        self.layout.addWidget(self.lbl_Answer,3,0)
        self.layout.addWidget(self._Answer,3,1,1,4)
        self.layout.addWidget(self.btnBrowse,3,5)
        self.layout.addWidget(self.btnCnlimage,3,6)
        self.layout.addWidget(self.chb_diff1,4,1)
        self.layout.addWidget(self.chb_diff2,4,2)
        self.layout.addWidget(self.btn_Problem,4,3)
        self.layout.addWidget(self.btn_Submit,4,4)
        self.layout.addWidget(self.btn_Exit,4,6)

    #making the browse button
    def singleBrowse(self):
         filepath = QFileDialog.getOpenFileName(self, 'Single File')
         list(filepath)
         if str(filepath[0]) != "":
             self.ImageForQ = []
             self.ImageForQ.append(str(filepath[0]))
             self.ImageForQ.append(str(filepath[0].split("/")[-1]))

    #restet image variable
    def resetImag(self):
        self.ImageForQ = ["",""]

    #to the Main Admin Screen
    def toMenu(self):
        global ex
        ex = maui.MainAWindow()
        ex.show()
        self.close()

    #submit the information
    def submit(self, diff, problem, answer):
        diffs = map(int, SubjectsDic[self.TopicName][1])
        if diff in diffs:
            folder = "%s\Topics" % os.getcwd()
            folder1 = "%s\Pictures" % os.getcwd()
            #testing to see if any fields are left blank
            prob = True
            ans = True
            if len(problem) == 0 or len(answer) == 0 or problem == " " or answer == " ":
                self.lbl_Error.setText("enter a valid problem or Answer")
            else:
                prev = " "
                for num in problem:
                    if num == prev and num == " ":
                        self.lbl_Error.setText("enter a valid problem")
                        prob = False
                    prev = num
                prev = " "
                for num in answer:
                    if num == prev and num == " ":
                        self.lbl_Error.setText("enter a valid answer")
                        ans = False
                    prev = num
                #the Line to be written to the file
                if str(self.ImageForQ[1]) != "":
                    #is the file a supported img file?
                    if str(self.ImageForQ[1])[-4:] == ".png" or str(self.ImageForQ[1])[-5:] == ".jpeg":
                        line = [problem, answer, str(self.ImageForQ[1])]
                        sht.copy(str(self.ImageForQ[0]), folder1)
                    else:
                        #set any to false to make satement false
                        ans = False
                        self.lbl_Error.setText("Not a supported img file")
                else:
                    line = [problem, answer, "null"]
                # if all tests are passed
                if prob and ans == True:
                    #is difficulty supported by topic?
                    Found = False
                    if diff in diffs:
                        for root, dirs, filenames in os.walk(folder):
                            for filename in filenames:
                                #does a file already exist with that difficulty?
                                if filename == "%s_%d.txt" % (self.TopicName, diff):
                                    Found = True
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
                    #one does not exist
                    else:
                        #create it and write to it
                        linebline = []
                        linebline.append(line)
                        File = open("%s\%s_%d.txt" % (folder,self.TopicName, diff),'w+')
                        for _ in range(0,len(linebline)):
                            if _ != len(linebline) - 1:
                                File.write("%s,%s,%s\n" % (linebline[_][0],linebline[_][1],linebline[_][2]))
                            else:
                                File.write("%s,%s,%s" % (linebline[_][0],linebline[_][1],linebline[_][2]))
                    self.toMenu()
        else:
            self.lbl_Error.setText("not a supported Diff")


    #Expands the window to include scientific notation
    def notation(self):
        if self.NotationOn == False:
            self.NotationOn = True
            #constructing the widget
            self.btnSquared = QPushButton("Power of", self)
            self.btnRooted = QPushButton("Root", self)
            #on clicked
            self.btnSquared.clicked.connect(lambda: self.Squared())
            self.btnRooted.clicked.connect(lambda: self.Rooted())
            #add to layout
            self.layout.addWidget(self.btnSquared,5,3)
            self.layout.addWidget(self.btnRooted,6,3)
        else:
            self.NotationOn = False
            self.layout.removeWidget(self.btnSquared)
            self.layout.removeWidget(self.btnRooted)
            self.btnSquared.deleteLater()
            self.btnRooted.deleteLater()
            self.btnSquared = None
            self.btnRooted = None

    #on Squared button clicked
    def Squared(self):
        if self.chb_diff1.isChecked():
            self._Problem.insertPlainText("@Power<>")
        else:
            currentT = self._Answer.text()
            self._Answer.setText("%s@Power<>" % currentT)

    #when the Root Button Is Pressed
    def Rooted(self):
        if self.chb_diff1.isChecked():
            self._Problem.insertPlainText("@Root{}")
        else:
            currentT = self._Answer.text()
            self._Answer.setText("%s@Root{}" % currentT)
