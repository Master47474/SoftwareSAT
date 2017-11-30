"""
Author: Marcus Facchino
Description:
    The Main file of this Program
"""

#Imports
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#File Imports
import MainUI as mui
import MenuUI as menui


#variables


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = mui.MainWindow()
    ex = menui.StartMenu()
    ex.show()
    sys.exit(app.exec_())
