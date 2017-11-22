"""
Author: Marcus Facchino
Description:
    The UI of the Main Window
"""

#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#File Imports


#variables
topics = []
topiclvl = {}

File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")

for subject in subjects:
    topic = subject.split(",")[0]
    difflvl = subject.split(",")[1:-1]
    topiclvl[topic] = difflvl
    topics.append(topic)


print topics
print topiclvl

class MainWindow(QMainWindow):
    #Init Function
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Problem Page')
        self.setWindowIcon(QIcon('placeholder.png'))

        self.makeMenuBar()
        self.makeDiffButtons()
        self.makeTopicRow()
        self.makeProblem()
        self.makeBottom()
        self.LayoutofP()

        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)
    # to Center the application
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #makes the menu bar
    def makeMenuBar(self):
        #make the menu bar
        self.menuBar = self.menuBar()
        #make a tabe under the menu Bar
        self.mbFile = self.menuBar.addMenu('&File')
        #make the tabs to gunder the file menu

        #problem Tab
        self.tabPromblem = QMenu('Problem', self)
        self.tabPNewP = QAction('New Problem', self)
        self.tabPSaveP = QAction('Save Problem', self)
        #Test tab
        self.tabTest = QMenu('Test', self)
        self.tabTNewT = QAction('New Test', self)
        self.tabTSaveT = QAction('Save Test', self)

        #adding the submenus to the problem tab
        self.tabPromblem.addAction(self.tabPNewP)
        self.tabPromblem.addAction(self.tabPSaveP)
        #adding the submenus to the Test tab
        self.tabTest.addAction(self.tabTNewT)
        self.tabTest.addAction(self.tabTSaveT)

        """ add all menus to the file tab """
        self.mbFile.addMenu(self.tabPromblem)
        self.mbFile.addMenu(self.tabTest)
    #makes tpoic label and serch bar
    def makeTopicRow(self):
        #topic and entering the topic
        self.lbl_Diff = QLabel("Difficulty :")
        self._Topic = QLineEdit()
        self._Topic.setPlaceholderText("Topic")
        self._Topic.setStyleSheet("QCustomLineEdit{color:gray;}")
        self._Topic.EchoMode(QLineEdit.Normal)
        self._Topic.setText("Topic")
        self._Topic.returnPressed.connect(lambda : self.TopicEntered())
    #makes difficulty buttons and assigns shit
    def makeDiffButtons(self):
        self.cbx_diff = QComboBox(self)
        self.cbx_diff.addItem("1")
        self.cbx_diff.addItem("2")
        self.cbx_diff.addItem("3")
        self.cbx_diff.addItem("4")
        self.cbx_diff.activated[int].connect(self.PrbBtnClicked)
    #make the problems section
    def makeProblem(self):
        self.lbl_Problem = QLabel(self)
        self.lbl_Problem.setText("This will be the problem")
        self.lbl_Problem.setStyleSheet("background-color: #E6E6E6; border: 1px inset grey;")
        self.lbl_Problem.setWordWrap(True)
        self.lbl_Problem.setAlignment(Qt.AlignTop)
        self.lbl_Problem.setMaximumSize(200,100)
        self.imgProblem = QLabel(self)
        self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/pythag1.png"))
        self.imgProblem.setScaledContents(True)
        self.imgProblem.setMaximumSize(300,300)
        self.lbl_answer = QLabel("Answer:", self)
        self.lbl_answer.setAlignment(Qt.AlignBottom)
        self._answer = QLineEdit()
    #make bottom
    def makeBottom(self):
        self.btnCheck = QPushButton("Check Answer", self)
        self.btnNextPrb = QPushButton("Next Question", self)
        self.btnExit = QPushButton("Exit", self)
        self.btnCheck.setMinimumHeight(40)
        self.btnNextPrb.setMinimumHeight(40)
        self.btnExit.setMinimumHeight(40)
    #the Layout of the Program
    def LayoutofP(self):
        # add on screen items
        self.layout = QGridLayout()
        self.layout.addWidget(self._Topic,0,0,1,2)
        self.layout.addWidget(self.lbl_Diff,0,2)
        self.layout.addWidget(self.cbx_diff,0,3)
        self.layout.addWidget(self.lbl_Problem,1,0,1,2)
        self.layout.addWidget(self.imgProblem,1,2,3,4)
        self.layout.addWidget(self.lbl_answer,2,0)
        self.layout.addWidget(self._answer,3,0,1,2)
        self.layout.addWidget(self.btnCheck,4,0)
        self.layout.addWidget(self.btnNextPrb,4,1)
        self.layout.addWidget(self.btnExit,4,5)

    """ functions for this to work """
    #when a difficulty button is clicked
    def PrbBtnClicked(self, inte):
        self.lbl_Problem.setText("%r" % inte)
    #when the topic is entered
    def TopicEntered(self):
        if self._Topic.text().lower() in topics:
            self.lbl_Problem.setText("%s" % self._Topic.text().lower())
        else:
            self.lbl_Problem.setText("%s does not exist or is spelt wrong" % self._Topic.text().lower())
