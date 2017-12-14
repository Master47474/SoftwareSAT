"""
Author: Marcus Facchino
Description:
    The UI of the Main Problem Window
"""

#Imports
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


#File Imports
import MenuUI as menui


#variables
topics = []
topiclvl = {}
questions = {}


File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")

class MainWindow(QMainWindow):
    #Init Function
    def __init__(self):
        super(MainWindow, self).__init__()
        #have to init
        self.Qcounter = 0

        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Problem Page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(500,400)

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
        File = open("Topics.txt",'r')
        FileR = File.read()
        subjects = FileR.split("\n")
        # reset variablesz
        topics = []
        topiclvl = {}
        questions = {}
        #topic and entering the topic
        self.lbl_Diff = QLabel("Difficulty :")
        self._Topic = QLineEdit()
        self._Topic.setPlaceholderText("Topic")
        self._Topic.setStyleSheet("QCustomLineEdit{color:gray;}")
        self._Topic.EchoMode(QLineEdit.Normal)
        self._Topic.setText("Topic")
        self._Topic.returnPressed.connect(lambda : self.TopicEntered())
        self.compl_topic = QCompleter()
        self._Topic.setCompleter(self.compl_topic)
        self.compl_list = QStringListModel()
        self.compl_topic.setModel(self.compl_list)
        for subject in subjects:
            topic = subject.split(",")[0]
            difflvl = subject.split(",")[1:-1]
            topiclvl[topic] = difflvl
            topics.append(topic)
        print topics
        self.compl_list.setStringList(topics)
    #makes difficulty buttons and assigns shit
    def makeDiffButtons(self):
        self.cbx_diff = QComboBox(self)
        self.cbx_diff.addItem("7")
        self.cbx_diff.addItem("8")
        self.cbx_diff.addItem("9")
        self.cbx_diff.addItem("10")
        self.cbx_diff.addItem("11")
        self.cbx_diff.addItem("12")
        self.cbx_diff.activated[int].connect(lambda: self.PrbBtnClicked(int(self.cbx_diff.currentText())))
    #make the problems section
    def makeProblem(self):
        self.lbl_Problem = QLabel(self)
        self.lbl_Problem.setText("This will be the problem")
        self.lbl_Problem.setStyleSheet("background-color: #E6E6E6; border: 1px inset grey;")
        self.lbl_Problem.setWordWrap(True)
        self.lbl_Problem.setAlignment(Qt.AlignTop)
        self.lbl_Problem.setMaximumSize(200,100)
        self.imgProblem = QLabel(self)
        #self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/pythag1.png"))
        self.imgProblem.setScaledContents(True)
        self.imgProblem.setMaximumSize(300,300)
        self.lbl_answer = QLabel("Answer:", self)
        self.lbl_answer.setAlignment(Qt.AlignBottom)
        self._answer = QLineEdit()
        self._answer.returnPressed.connect(lambda : self.btncheck())
        self._answer.EchoMode(QLineEdit.Normal)
    #make bottom
    def makeBottom(self):
        self.btnCheck = QPushButton("Check Answer", self)
        self.btnNextPrb = QPushButton("Next Question", self)
        self.btnExit = QPushButton("Exit", self)
        self.btnCheck.setMinimumHeight(40)
        self.btnNextPrb.setMinimumHeight(40)
        self.btnExit.setMinimumHeight(40)
        self.btnCheck.clicked.connect(lambda: self.btncheck())
        self.btnNextPrb.clicked.connect(lambda: self.btnNextQuestion())
        self.btnExit.clicked.connect(lambda: self.toMenu())
    #check if answer is right
    def btncheck(self):
        try:
            if int(self._answer.text()) == int(questions[self.Qcounter][2]):
                self._answer.setText("RIGHT WOOOO, dare try another?")
            else:
                self._answer.setText("WRONGGG")
        except:
            self._answer.setText("BOIIII put numbers in here")
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
    # making the question look good"
    def formQuestion(self, file):
        counter = 0
        for question in file:
            statement =  question.split(",")[0]
            Qquestion = question.split(",")[1]
            answer = question.split(",")[2]
            img = question.split(",")[3]
            Both = []
            Both.append(statement)
            Both.append(Qquestion)
            Both.append(answer)
            Both.append(img)
            questions[counter] = Both
            counter += 1
        html_code = """\
                    <h5>{HTStatement}</h5>
                    {HTQuestion}
                    """.format(HTStatement=questions[self.Qcounter][0],HTQuestion=questions[self.Qcounter][1])
        self.lbl_Problem.setText(html_code)
        if questions[self.Qcounter][3] != "null":
            self.imgProblem.setPixmap(QPixmap(os.getcwd() + "%s" % questions[self.Qcounter][3]))
        else:
            self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/null.png"))
    #when a difficulty button is clicked
    def PrbBtnClicked(self, inte):
        try:
            self.Qcounter = 0
            self.Topic_File = open(os.getcwd() + "/Topics/%s_%r.txt" % (str(self._Topic.text().lower()), inte), "r")
            self.fileR = self.Topic_File.read()
            self.questionRows = self.fileR.split("\n")
            self.formQuestion(self.questionRows)
        except:
            self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/null.png"))
            self.lbl_Problem.setText("That Topic in that Difficulty does not exit. maybe try another?")
    #when the topic is entered
    def TopicEntered(self):
        if self._Topic.text().lower() in topics:
            self.lbl_Problem.setText("%s" % self._Topic.text().lower())
            self.Qcounter = 0
        else:
            self.lbl_Problem.setText("%s does not exist or is spelt wrong" % self._Topic.text().lower())
    #when next question button is clicked
    def btnNextQuestion(self):
        try:
            self.Qcounter += 1
            html_code = """\
                        <h5>{HTStatement}</h5>
                        {HTQuestion}
                        """.format(HTStatement=questions[self.Qcounter][0],HTQuestion=questions[self.Qcounter][1])
            self.lbl_Problem.setText(html_code)
            self._answer.setText("")
            if questions[self.Qcounter][3] != "null":
                self.imgProblem.setPixmap(QPixmap(os.getcwd() + "%s" % questions[self.Qcounter][3]))
            else:
                self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/null.png"))
        except:
            self.lbl_Problem.setText("uh oh there seems to be no more Questions. or something went wrong!")
    #back to main screen
    def toMenu(self):
        ex = menui.StartMenu()
        ex.show()
        self.close()
