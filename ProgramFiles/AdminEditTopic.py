
"""
Author: Marcus Facchino
Description:
    The UI of the Edit Topic Window
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
        self.setWindowTitle('Testing UI For Edit Topic menu page')
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
        self.lbl_TopicChange = QLabel("Change Topic Name:")
        self.lbl_TopicDChange = QLabel("Add or Remove Topic Difficulties:")
        self._TopicName = QLineEdit()
        self.btnExit = QPushButton("Exit", self)
        self.btnConfirm = QPushButton("Confirm", self)
        self.btnDelete = QPushButton("Delete!", self)
        self.chb_diff1 = QCheckBox("7",self)
        self.chb_diff2 = QCheckBox("8",self)
        self.chb_diff3 = QCheckBox("9",self)
        self.chb_diff4 = QCheckBox("10",self)
        self.chb_diff5 = QCheckBox("11",self)
        self.chb_diff6 = QCheckBox("12",self)
        #list of all checkboxes
        cbx = [self.chb_diff1,self.chb_diff2,self.chb_diff3,self.chb_diff4,self.chb_diff5,self.chb_diff6]
        #remaking the Dictionary incase of anychanges
        SubjectsDic = self.Splittting()
        #should chekcbox start ticked?
        for num in range(0,len(cbx)):
            if int(SubjectsDic[str(self.TopicName)][1][num]) != 0:
                cbx[num].setChecked(True)
        #cosmetic effects fo Ui elements
        self._TopicName.setMaxLength(20)
        self.lbl_TopicN.setAlignment(Qt.AlignCenter)
        self.lbl_TopicN.setStyleSheet("QLabel {background-color: grey;}")
        self.lbl_TopicN.setFixedHeight(50)
        self.btnExit.setMinimumHeight(30)
        self.btnConfirm.setMinimumHeight(30)
        self.btnDelete.setMinimumHeight(30)
        #on button clicked
        self.btnExit.clicked.connect(lambda: self.toMenu())
        self.btnConfirm.clicked.connect(lambda: self.confirm())
        self.btnDelete.clicked.connect(lambda: self.Delete())

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
        self.layout.addWidget(self.btnDelete,3,0)
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

    """getting rid of a difficulty, when tehres a file for it!!!"""
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
        for num in str(self._TopicName.text()):
            if num == prev and num == " ":
                print "enter a valid name"
                break
            else:
                #if the last letter is == to the last letter of the topic
                if num == str(self._TopicName.text())[-1]:
                    #get the folder holding the files
                    folder = "%s\Topics" %os.getcwd()
                    #replace name with new name
                    SubjectsDic[str(self.TopicName)] = ("%s" % str(self._TopicName.text()).lower(),) + SubjectsDic[str(self.TopicName)][1:]
                    #changeing the file names of any files accociated with old name to new name
                    for root, dirs, filenames in os.walk(folder):
                        for filename in filenames:
                            #i have no clue what this is cause i stole this line from stack overflow, all i kow is that it gets all the file paths and makes into a list
                            pathiter = (os.path.join(root, filename) for root, _, filenames in os.walk(folder) for filename in filenames)
                            for path in pathiter:
                                #if it starts with the topic name
                                if filename.startswith(str(self.TopicName)):
                                    try:
                                        #rename it
                                        newname = path.replace("%s_%d.txt" % (self.TopicName, int(filename[len(self.TopicName)+1:-3])), "%s_%d.txt" % (SubjectsDic[self.TopicName][0]\
                                                                                                        , int(filename[len(self.TopicName)+1:-3])))
                                        #put it back in its original place
                                        if newname != path:
                                            os.rename(path, newname)
                                    #have a 2 didget number at the end i.e _10 not _9
                                    except:
                                        #rename it
                                        newname = path.replace("%s_%d.txt" % (self.TopicName, int(filename[len(self.TopicName)+1:-4])), "%s_%d.txt" % (SubjectsDic[self.TopicName][0]\
                                                                                                        , int(filename[len(self.TopicName)+1:-4])))
                                        #put it back in its original place
                                        if newname != path:
                                            os.rename(path, newname)

                prev = num
        try:
            #looking over the checkboxes to give values to valid difficulties
            folder = "%s\Topics" %os.getcwd()
            dellist = []
            for num in range(0,len(cbx)):
                if cbx[num].isChecked():
                    SubjectsDic[str(self.TopicName)][1][num] = int(cbx[num].text())
                else:
                    if int(SubjectsDic[str(self.TopicName)][1][num]) != 0:
                        dellist.append(num+7)
                    else:
                        SubjectsDic[str(self.TopicName)][1][num] = 0
            self.ConfirmDel(*dellist)
        except:
            print "failed with check boxes"
        #ordering the topic names
        ordered = {}
        for key in sorted(SubjectsDic.iterkeys()):
            ordered[key] = SubjectsDic[key]
        File = File = open("Topics.txt",'w')
        counter = 0
        #Writing back to topics file with new names and diff values
        for line in ordered:
            if counter == len(ordered) - 1:
                File.write("%s,%d,%d,%d,%d,%d,%d" % (SubjectsDic[line][0],int(SubjectsDic[line][1][0]),\
                                                        int(SubjectsDic[line][1][1]),int(SubjectsDic[line][1][2]),\
                                                        int(SubjectsDic[line][1][3]),int(SubjectsDic[line][1][4]),int(SubjectsDic[line][1][5])))
            else:
                File.write("%s,%d,%d,%d,%d,%d,%d\n" % (SubjectsDic[line][0],int(SubjectsDic[line][1][0]),\
                                                    int(SubjectsDic[line][1][1]),int(SubjectsDic[line][1][2]),\
                                                    int(SubjectsDic[line][1][3]),int(SubjectsDic[line][1][4]),int(SubjectsDic[line][1][5])))
            counter += 1
        File.close()
        self.toMenu()

    #abou to delete a folder when confirming
    def ConfirmDel(self, *diffs):
        diffs = list(diffs)
        if len(diffs) >= 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Warning!")
            msg.setInformativeText("You are about to Delete topic files accociated with  %s" % self.TopicName)
            msg.setWindowTitle("WARNING")
            folder = "%s\Topics" % os.getcwd()
            items = []
            #make the detailed msg
            for num in range(7,12):
                print num
                if num in diffs:
                    items.append("Diffuculty: %d" % num)
            #makes the Detailed msg with all info such as topic name and what files will be deleted
            detailedmsg = "Topic: %s\n%s" % (self.TopicName,'\n'.join(map(str, items)))
            msg.setDetailedText(detailedmsg)
            #what buttons will be on screen
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(self.confbtn)
            self.retval = msg.exec_()

    def confbtn(self,i):
        #SubjectsDic = self.Splittting()
        if i.text() == "OK":
            folder = "%s\Topics" %os.getcwd()
            cbx = [self.chb_diff1,self.chb_diff2,self.chb_diff3,self.chb_diff4,self.chb_diff5,self.chb_diff6]
            for num in range(0,len(cbx)):
                if cbx[num].isChecked():
                    pass
                else:
                    for root, dirs, filenames in os.walk(folder):
                        for filename in filenames:
                            if filename == "%s_%d.txt" % (str(self.TopicName), int(SubjectsDic[str(self.TopicName)][1][num])):
                                os.remove(os.path.join(folder, filename))
                                print "remove"
                    SubjectsDic[str(self.TopicName)][1][num] = 0



    #deletes Topic and All aocociated files
    def Delete(self):
        if self.TopicName in SubjectsDic:
            #makes pop up box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Warning!")
            msg.setInformativeText("You are about to Delete %s and all of the files Accociated with it" % self.TopicName)
            msg.setWindowTitle("WARNING")
            folder = "%s\Topics" % os.getcwd()
            items = []
            #looks for and if there are any files
            for root, dirs, filenames in os.walk(folder):
                for filename in filenames:
                    if filename.startswith(str(self.TopicName)):
                        try:
                            items.append(str("Diffuculty: %d" % int(filename[len(self.TopicName)+1:-4])))
                        except:
                            items.append(str("Diffuculty: %d" % int(filename[len(self.TopicName)+1:-4])))
            #makes the Detailed msg with all info such as topic name and what files will be deleted
            detailedmsg = "Topic: %s\n%s" % (self.TopicName,'\n'.join(map(str, items)))
            msg.setDetailedText(detailedmsg)
            #what buttons will be on screen
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(self.msgbtn)
            self.retval = msg.exec_()

    #when a button on the pop up is clicked
    def msgbtn(self,i):
        #was it the ok button?
        if i.text() == "OK":
            folder = "%s\Topics" % os.getcwd()
            #deleting all files in the topics folder accociated with the topic
            for root, dirs, filenames in os.walk(folder):
                for filename in filenames:
                    if filename.startswith(str(self.TopicName)):
                        try:
                            os.remove(os.path.join(folder,filename))
                        except:
                            print "error"
            #resplitting
            SubjectsDic = self.Splittting()
            #deleting the subject from the dirctionary
            del SubjectsDic[self.TopicName]
            #reordreing and writing back to the file with new Dict
            ordered = {}
            for key in sorted(SubjectsDic.iterkeys()):
                ordered[key] = SubjectsDic[key]
            File = File = open("Topics.txt",'w')
            counter = 0
            for line in ordered:
                if counter == len(ordered) - 1:
                    File.write("%s,%d,%d,%d,%d,%d,%d" % (SubjectsDic[line][0],int(SubjectsDic[line][1][0]),\
                                                            int(SubjectsDic[line][1][1]),int(SubjectsDic[line][1][2]),\
                                                            int(SubjectsDic[line][1][3]),int(SubjectsDic[line][1][4]),int(SubjectsDic[line][1][5])))
                else:
                    File.write("%s,%d,%d,%d,%d,%d,%d\n" % (SubjectsDic[line][0],int(SubjectsDic[line][1][0]),\
                                                        int(SubjectsDic[line][1][1]),int(SubjectsDic[line][1][2]),\
                                                        int(SubjectsDic[line][1][3]),int(SubjectsDic[line][1][4]),int(SubjectsDic[line][1][5])))
                counter += 1
            File.close()
            self.toMenu()
        else:
            print "Button pressed is:", i.text()

    #To the Main Admin Menu
    def toMenu(self):
        ex = maui.MainAWindow()
        ex.show()
        self.close()
