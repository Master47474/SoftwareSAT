
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
import AdminEditTopic as ateui
import AddQuestionUI as aqui
import EditQuestionsUI as equi
import AddTopicUI as addtui


#variables
#getting each row of the topics file
File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")

class MainAWindow(QMainWindow):
    #init
    def __init__(self, Topic):
        super(MainAWindow, self).__init__()
        self.TopicMain = Topic
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Admin menu page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(400,300)
        #creatds the ui Elements
        self.createBtns()
        #layout the program
        self.LayoutofP()

        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)

    #centers the Application
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #creates the UI Elements of the window
    def createBtns(self):
        self.lbl_Topic = QLabel("select a topic:")
        self.cbx_topics = QComboBox(self)
        self.btn_EditT = QPushButton("Edit Topic",self)
        self.btn_EditQ = QPushButton("Edit Question",self)
        self.btn_AddQ = QPushButton("Add Question",self)
        self.btn_AddT = QPushButton("Add Topic",self)
        self.btnExit = QPushButton("Exit", self)
        #Re Spliitng fiel incase of changes
        File = open("Topics.txt",'r')
        FileR = File.read()
        subjects = FileR.split("\n")
        #getting the topic names and populating the dropdown box with names
        for subject in subjects:
            self.cbx_topics.addItem(str(subject.split(",")[0]))
        #cosmetic effects
        self.lbl_Topic.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.btnExit.setMinimumHeight(40)
        #maitnience
        alltopics = [self.cbx_topics.itemText(i) for i in range(self.cbx_topics.count())]
        for _ in range(0,len(alltopics)):
            if self.TopicMain == alltopics[_]:
                self.cbx_topics.setCurrentIndex(_)
                break
            else:
                self.cbx_topics.setCurrentIndex(0)
        #on clciked
        self.btnExit.clicked.connect(lambda: self.toMenu())
        self.btn_EditT.clicked.connect(lambda: self.toEditTop())
        self.btn_AddQ.clicked.connect(lambda: self.toAddQ())
        self.btn_EditQ.clicked.connect(lambda: self.toEditQ())
        self.btn_AddT.clicked.connect(lambda: self.toAddT())


    #laysout the program
    def LayoutofP(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.lbl_Topic,0,0)
        self.layout.addWidget(self.cbx_topics,0,1)
        self.layout.addWidget(self.btn_AddQ,1,0)
        self.layout.addWidget(self.btn_EditQ,2,0)
        self.layout.addWidget(self.btn_AddT,1,2)
        self.layout.addWidget(self.btn_EditT,2,2)
        self.layout.addWidget(self.btnExit,4,2)

    #to the Menu Window
    def toMenu(self):
        global ex
        ex = menui.StartMenu()
        ex.show()
        self.close()

    #to the Edit Topic Window
    def toEditTop(self):
        global ex
        ex = ateui.MainWindow(self.cbx_topics.currentText())
        ex.show()
        self.close()

    #to the Add Question Window
    def toAddQ(self):
        global ex
        ex = aqui.MainWindow(self.cbx_topics.currentText())
        ex.show()
        self.close()

    #to the Edit Question Window
    def toAddT(self):
        global ex
        ex = addtui.MainWindow(self.cbx_topics.currentText())
        ex.show()
        self.close()

    #to the Edit Question Window
    def toEditQ(self):
        global ex
        ex = equi.MainWindow(self.cbx_topics.currentText())
        ex.show()
        self.close()
