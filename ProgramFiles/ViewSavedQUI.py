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
import MainUI as mainui
import SavedProblemsUI as spui

#Variables
File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")
File.close()




class MainWindow(QMainWindow):
    #init
    def __init__(self):
        super(MainWindow, self).__init__()
        #setting the Topic name chosen at the Previous screen
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
        self.lbl_TopicN = QLabel("Load Questions")
        self.lbl_filter = QLabel("Filters:")
        self.chb_diff1 = QCheckBox("7",self)
        self.chb_diff2 = QCheckBox("8",self)
        self.chb_diff3 = QCheckBox("9",self)
        self.chb_diff4 = QCheckBox("10",self)
        self.chb_diff5 = QCheckBox("11",self)
        self.chb_diff6 = QCheckBox("12",self)
        self.chb_All= QCheckBox("All",self)
        self.lbl_topics = QLabel("Topics:", self)
        self.cbx_topics = QComboBox(self)
        #Re Spliitng fiel incase of changes
        File = open("Topics.txt",'r')
        FileR = File.read()
        subjects = FileR.split("\n")
        #getting the topic names and populating the dropdown box with names
        for subject in subjects:
            self.cbx_topics.addItem(str(subject.split(",")[0]))
        self.chbList = [self.chb_diff1,self.chb_diff2,self.chb_diff3,self.chb_diff4,self.chb_diff5,self.chb_diff6]
        for chb in self.chbList:
            chb.setChecked(True)
        self.btnApplyFilter = QPushButton("Apply Filter", self)
        self.lblQuestions = QLabel("Questions:")
        self.btn_Exit = QPushButton("Exit", self)
        #cosmetic effects fo Ui elements1
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.lbl_TopicN.setFixedHeight(50)
        #assign buttons
        self.btnApplyFilter.clicked.connect(lambda: self.makeQuesitonlist())
        self.btn_Exit.clicked.connect(lambda: self.toMenu())
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
        mygroupbox = QGroupBox("Topic, Difficulty, Question, Answer")
        self.myform = QVBoxLayout()
        files = []
        folder = "%s\SavedTopics" % os.getcwd()
        #are there any files for this topic?
        Found = False
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if self.chb_All.isChecked():
                    Found = True
                    files.append(filename)
                else:
                    #does a file already exist with that difficulty?
                    if filename.startswith("%s" % self.cbx_topics.currentText()):
                        Found = True
                        files.append(filename)
        self.FinalQuestions = []
        self.FinalButtons = QButtonGroup()
        self.FinalButtons.buttonClicked[QAbstractButton].connect(self.EditBtnClicked)
        #was at least one found?
        if Found == True:
            #init the line no.
            line = 1
            buttons = {}
            for filename in files:
                try:
                    diff = int(filename[-6:-4])
                except:
                    diff = int(filename[-5])
                if diff in self.filter:
                    #read the file and get the questions
                    File = open("%s\%s" % (folder, filename),'r')
                    FileR = File.read()
                    Questions = FileR.split("\n")
                    #for each question, get the diff,text,answer and append and make it a row
                    for question in Questions:
                        linebline = []
                        linebline.append(question.split(","))
                        for _ in range(0,len(linebline)):
                            try:
                                textT = linebline[_][0]
                                answerT = linebline[_][1]
                                if len(linebline[_][0]) > 25:
                                    linebline[_][0] = "%s..." % linebline[_][0][0:25]
                                text = linebline[_][0]
                                self.list2append = [line, '%s | %d, %s' % (filename[0:-13],diff,text), textT, answerT, linebline[_][2]]
                                self.FinalQuestions.append(self.list2append)
                                line += 1
                            except:
                                pass
            for line in range(0,line - 1):
                btnEd = QPushButton("To Problem %s" % self.FinalQuestions[line][0])
                btnEd.setFixedWidth(125)
                self.FinalButtons.addButton(btnEd)
                hbox = QHBoxLayout()
                hbox.addWidget(QLabel(self.FinalQuestions[line][1]))
                hbox.addWidget(btnEd)
                self.myform.addItem(hbox)
        mygroupbox.setLayout(self.myform)
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
        self.layout.addWidget(self.lbl_topics,2,0)
        self.layout.addWidget(self.cbx_topics,2,1,1,4)
        self.layout.addWidget(self.chb_All,2,5)
        self.layout.addWidget(self.btnApplyFilter,2,6)
        self.layout.addWidget(self.lblQuestions,3,0)
        self.layout.addWidget(self.scroll,4,0,4,12)
        self.layout.addWidget(self.btn_Exit,10,11)


    def EditBtnClicked(self, button):
        """ set import """
        ex = spui.MainWindow(self.FinalQuestions[int(button.text()[10:])-1][2], self.FinalQuestions[int(button.text()[10:])-1][3]\
                                ,self.FinalQuestions[int(button.text()[10:])-1][4])
        ex.show()
        self.close()

    #to the Main Admin Screen
    def toMenu(self):
        global ex
        ex = mainui.MainWindow()
        ex.show()
        self.close()
