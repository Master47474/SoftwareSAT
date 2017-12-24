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
import re


#File Imports
import MenuUI as menui


#variables
topics = []
topiclvl = {}
questions = {}

#Spliting the file into Topics (one per row)
File = open("Topics.txt",'r')
FileR = File.read()
subjects = FileR.split("\n")

#main window
class MainWindow(QMainWindow):
    #Init Function
    def __init__(self):
        super(MainWindow, self).__init__()
        #init Variables
        self.Qcounter = 0
        self.questions = {}
        self.initUI()

    def initUI(self):
        #Window Specs
        self.center()
        self.setWindowTitle('Testing UI For Problem Page')
        self.setWindowIcon(QIcon('placeholder.png'))
        self.resize(500,400)

        #makes the elements of the UI
        self.makeMenuBar()
        self.makeDiffButtons()
        self.makeTopicRow()
        self.makeProblem()
        self.makeBottom()
        #layouts the elements
        self.LayoutofP()

        Widget_M = QWidget()
        Widget_M.setLayout(self.layout)
        self.setCentralWidget(Widget_M)

    #Center the Window on screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        #moving the window to center
        self.move(qr.topLeft())

    #makes the menu bar
    def makeMenuBar(self):
        #make the menu bar
        self.menuBar = self.menuBar()
        #make a tabe under the menu Bar
        self.mbFile = self.menuBar.addMenu('&File')

        #make the tabs to go under the file menu
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

        #add all menus to the file tab
        self.mbFile.addMenu(self.tabPromblem)
        self.mbFile.addMenu(self.tabTest)

    #makes topic label and search bar
    def makeTopicRow(self):
        #resplitting file in case of any changes to topic file
        File = open("Topics.txt",'r')
        FileR = File.read()
        subjects = FileR.split("\n")
        #reset variables
        topics = []
        topiclvl = {}
        questions = {}
        #topic and entering the topic
        self.lbl_Diff = QLabel("Difficulty :")
        self._Topic = QLineEdit()
        self._Topic.setPlaceholderText("Topic")
        #cosmetic effects to UI Elements
        self._Topic.setStyleSheet("QCustomLineEdit{color:gray;}")
        self._Topic.EchoMode(QLineEdit.Normal)
        self._Topic.setText("Topic")
        self.compl_topic = QCompleter()
        self._Topic.setCompleter(self.compl_topic)
        self.compl_list = QStringListModel()
        self.compl_topic.setModel(self.compl_list)
        #on _topic enter pressed
        self._Topic.returnPressed.connect(lambda : self.TopicEntered())
        #getting the topic names of each row
        for subject in subjects:
            topic = subject.split(",")[0]
            difflvl = subject.split(",")[1:-1]
            topiclvl[topic] = difflvl
            topics.append(topic)
        #for auto fill
        self.compl_list.setStringList(topics)

    #makes difficulty buttons and populates it
    def makeDiffButtons(self):
        self.cbx_diff = QComboBox(self)
        #populates the Dropdown box
        self.cbx_diff.addItem("7")
        self.cbx_diff.addItem("8")
        self.cbx_diff.addItem("9")
        self.cbx_diff.addItem("10")
        self.cbx_diff.addItem("11")
        self.cbx_diff.addItem("12")
        #on a number clicked
        self.cbx_diff.activated[int].connect(lambda: self.PrbBtnClicked(int(self.cbx_diff.currentText())))

    #make the problems section
    def makeProblem(self):
        #init Ui Elements
        self.lbl_Problem = QLabel(self)
        self.lbl_answer = QLabel("Answer:", self)
        self.imgProblem = QLabel(self)
        self._answer = QLineEdit()
        #Cosmetic effects to Elements
        self.lbl_Problem.setText("This will be the problem")
        self.lbl_Problem.setStyleSheet("background-color: #E6E6E6; border: 1px inset grey;")
        self.lbl_Problem.setWordWrap(True)
        self.lbl_Problem.setAlignment(Qt.AlignTop)
        self.lbl_Problem.setAlignment(Qt.AlignLeft)
        self.lbl_Problem.setMaximumSize(200,100)
        self.imgProblem.setScaledContents(True)
        self.imgProblem.setMaximumSize(300,300)
        self.lbl_answer.setAlignment(Qt.AlignBottom)
        #on _Answer Enter pressed
        self._answer.returnPressed.connect(lambda : self.btncheck())
        self._answer.EchoMode(QLineEdit.Normal)

    #make bottom of problem page
    def makeBottom(self):
        #init Ui Elements
        self.btnCheck = QPushButton("Check Answer", self)
        self.btnNextPrb = QPushButton("Next Question", self)
        self.btnExit = QPushButton("Exit", self)
        #cosmetic effects to UI Elements
        self.btnCheck.setMinimumHeight(40)
        self.btnNextPrb.setMinimumHeight(40)
        self.btnExit.setMinimumHeight(40)
        #on button clicked
        self.btnCheck.clicked.connect(lambda: self.btncheck())
        self.btnNextPrb.clicked.connect(lambda: self.btnNextQuestion())
        self.btnExit.clicked.connect(lambda: self.toMenu())


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

    """ functions not do do with UI """

    #on Answer button clicked, Check answer
    def btncheck(self):
        #if answer entered == Answer in file
        if self._answer.text() == self.questions[self.Qcounter][1]:
            self._answer.setText("RIGHT WOOOO, dare try another?")
        else:
            self._answer.setText("WRONGGG")


    # Forming the question on the screen
    def formQuestion(self, file):
        self.questions = {}
        counter = 0
        #getting the Question
        for question in file:
            statement =  question.split(",")[0]
            Qquestion = question.split(",")[1]
            img = question.split(",")[2]
            #translating text into html code to be able to show mathematical notaion
            self.FindRoot(statement, Qquestion)
            statement = self.Rootproblem
            Qquestion = self.Rootanswer
            self.FindPower(statement, Qquestion)
            statement = self.PowerProblem
            Qquestion = self.PowerAnswer
            Both = []
            Both.append(statement)
            Both.append(Qquestion)
            Both.append(img)
            self.questions[counter] = Both
            counter += 1
        #Making the Question pretty with the ablitiy to have math notation
        html_code = """{HTStatement}""".format(HTStatement=self.questions[self.Qcounter][0])
        self.lbl_Problem.setText(html_code)
        #is there a picture for this problem?
        if self.questions[self.Qcounter][2] != "null":
            self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/%s" % self.questions[self.Qcounter][2]))
        else:
            self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/null.png"))

    #when a difficulty button is clicked
    def PrbBtnClicked(self, inte):
        try:
            self.Qcounter = 0
            #open a file with from that topic with the topic difficulty
            self.Topic_File = open(os.getcwd() + "/Topics/%s_%r.txt" % (str(self._Topic.text().lower()), inte), "r")
            self.fileR = self.Topic_File.read()
            self.questionRows = self.fileR.split("\n")
            self.formQuestion(self.questionRows)
        #cant find s file with that difficulty
        except:
            self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/null.png"))
            self.lbl_Problem.setText("That Topic in that Difficulty does not exit. maybe try another?")

    #If Topic is entered manually without autocompletion
    def TopicEntered(self):
        #make text lowercase so its easier for people to enter topic name
        if self._Topic.text().lower() in topics:
            self.lbl_Problem.setText("%s" % self._Topic.text().lower())
            self.Qcounter = 0
        #cant find topic
        else:
            self.lbl_Problem.setText("%s does not exist or is spelt wrong" % self._Topic.text().lower())

    #when next question button is clicked
    def btnNextQuestion(self):
        try:
            self.Qcounter += 1
            #set new question on screen
            html_code = """{HTStatement}""".format(HTStatement=self.questions[self.Qcounter][0])
            self.lbl_Problem.setText(html_code)
            #is there a picture for this problem?
            if self.questions[self.Qcounter][2] != "null":
                self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/%s" % self.questions[self.Qcounter][2]))
            else:
                self.imgProblem.setPixmap(QPixmap(os.getcwd() + "/Pictures/null.png"))
        #cant find anymore Questions
        except:
            self.lbl_Problem.setText("uh oh there seems to be no more Questions. or something went wrong!")

    #back to main screen
    def toMenu(self):
        global ex
        ex = menui.StartMenu()
        ex.show()
        self.close()

    #finding and translating the equation with roots into something readable
    def FindRoot(self, problem, answer):
        #for problem
        self.Rootproblem = problem
        self.foundRoots = re.findall(r'@(Root{[^}]*})', str(self.Rootproblem))
        for root in self.foundRoots:
            root = root[5:-1]
            rooted = "<span style='white-space: nowrap; font-size:larger'>&radic;<span style='text-decoration:overline;'>&nbsp;%s&nbsp;</span></span>" % root
            self.Rootproblem = re.sub(r'@(Root{[^}]*})', rooted, self.Rootproblem, count=1, flags=0)

        self.Rootanswer = answer
        self.foundRoots = re.findall(r'@(Root{[^}]*})', str(self.Rootanswer))
        for root in self.foundRoots:
            root = root[5:-1]
            rooted = "<span style='white-space: nowrap; font-size:larger'>&radic;<span style='text-decoration:overline;'>&nbsp;%s&nbsp;</span></span>" % root
            self.Rootanswer = re.sub(r'@(Root{[^}]*})', rooted, self.Rootanswer, count=1, flags=0)

    # finding and translating an equation into soomethoing redabnle
    def FindPower(self, problem, answer):
        #for problem
        self.PowerProblem = problem
        self.foundPowers = re.findall(r'@(Power<[^>]*>)', str(self.PowerProblem))
        for power in self.foundPowers:
            power = power[6:-1]
            powered = "<sup>%s</sup>" % power
            self.PowerProblem = re.sub(r'@(Power<[^>]*>)', powered, self.PowerProblem, count=1, flags=0)

        self.PowerAnswer = answer
        self.foundPowers = re.findall(r'@(Power<[^>]*>)', str(self.PowerProblem))
        for power in self.foundPowers:
            power = power[6:-1]
            powered = "<sup>%s</sup>" % power
            self.PowerAnswer = re.sub(r'@(Power<[^>]*>)', powered, self.PowerAnswer, count=1, flags=0)
