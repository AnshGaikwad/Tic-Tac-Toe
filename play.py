# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyttsx3
import webbrowser

plyFlag = 0
plyScr1 = 0
plyScr2 = 0
mode = ' '
board = [' ' for x in range(10)]
win = False


class Ui_MainWindow(object):

    # Function converted into code from PyQt5 designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 466)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 93, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 125, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 93, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 125, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 93, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 93, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 125, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 93, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 93, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 187, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 40, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 40, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 150, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 150, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 150, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 260, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 260, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 260, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 70, 371, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 180, 371, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(590, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 26))
        self.menubar.setObjectName("menubar")
        self.menuNew_Game = QtWidgets.QMenu(self.menubar)
        self.menuNew_Game.setObjectName("menuNew_Game")
        self.menuExtras = QtWidgets.QMenu(self.menubar)
        self.menuExtras.setObjectName("menuExtras")
        self.menuOthers = QtWidgets.QMenu(self.menubar)
        self.menuOthers.setObjectName("menuOthers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHuman = QtWidgets.QAction(MainWindow)
        self.actionHuman.setObjectName("actionHuman")
        self.actionhuman_plays_first = QtWidgets.QAction(MainWindow)
        self.actionhuman_plays_first.setObjectName("actionhuman_plays_first")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionComputer_2 = QtWidgets.QAction(MainWindow)
        self.actionComputer_2.setObjectName("actionComputer_2")
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionLinkedIn = QtWidgets.QAction(MainWindow)
        self.actionLinkedIn.setObjectName("actionLinkedIn")
        self.menuNew_Game.addSeparator()
        self.menuNew_Game.addAction(self.actionHuman)
        self.menuNew_Game.addAction(self.actionComputer_2)
        self.menuExtras.addAction(self.actionInstructions)
        self.menuExtras.addAction(self.actionCredits)
        self.menuOthers.addAction(self.actionGithub)
        self.menuOthers.addAction(self.actionLinkedIn)
        self.menubar.addAction(self.menuNew_Game.menuAction())
        self.menubar.addAction(self.menuExtras.menuAction())
        self.menubar.addAction(self.menuOthers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Disabling push buttons at initial state
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_11.setEnabled(False)

        # Defining on click methods
        self.pushButton_10.clicked.connect(lambda: self.resetBoard())
        self.pushButton_11.clicked.connect(lambda: self.resetScore())
        self.pushButton.clicked.connect(lambda: self.btnClk(1))
        self.pushButton_2.clicked.connect(lambda: self.btnClk(2))
        self.pushButton_3.clicked.connect(lambda: self.btnClk(3))
        self.pushButton_4.clicked.connect(lambda: self.btnClk(4))
        self.pushButton_5.clicked.connect(lambda: self.btnClk(5))
        self.pushButton_6.clicked.connect(lambda: self.btnClk(6))
        self.pushButton_7.clicked.connect(lambda: self.btnClk(7))
        self.pushButton_8.clicked.connect(lambda: self.btnClk(8))
        self.pushButton_9.clicked.connect(lambda: self.btnClk(9))

        # Defining on Trigger Methods
        self.actionHuman.triggered.connect(lambda: self.human())
        self.actionComputer_2.triggered.connect(lambda: self.comp())
        self.actionGithub.triggered.connect(lambda: self.github())
        self.actionLinkedIn.triggered.connect(lambda: self.linkedin())
        self.actionCredits.triggered.connect(lambda: self.credits())
        self.actionInstructions.triggered.connect(lambda: self.instructions())

    # Function converted into code from PyQt5 designer
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to Tic-Tac-Toe"))
        self.pushButton.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_7.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_9.setShortcut(_translate("MainWindow", "9"))
        self.label.setText(_translate("MainWindow", "Player X: 0"))
        self.label_2.setText(_translate("MainWindow", "Player O: 0"))
        self.pushButton_10.setText(_translate("MainWindow", "Board Reset"))
        self.pushButton_10.setShortcut(_translate("MainWindow", "R"))
        self.pushButton_11.setText(_translate("MainWindow", "Score Reset"))
        self.pushButton_11.setShortcut(_translate("MainWindow", "S"))
        self.menuNew_Game.setTitle(_translate("MainWindow", "New Game"))
        self.menuExtras.setTitle(_translate("MainWindow", "Extras"))
        self.menuOthers.setTitle(_translate("MainWindow", "Links"))
        self.actionHuman.setText(_translate("MainWindow", "Human"))
        self.actionHuman.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionInstructions.setShortcut(_translate("MainWindow", "I"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionCredits.setShortcut(_translate("MainWindow", "C"))
        self.actionComputer_2.setText(_translate("MainWindow", "Computer"))
        self.actionComputer_2.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionGithub.setText(_translate("MainWindow", "Source Code"))
        self.actionGithub.setShortcut(_translate("MainWindow", "S"))
        self.actionLinkedIn.setText(_translate("MainWindow", "Developer Info"))
        self.actionLinkedIn.setShortcut(_translate("MainWindow", "D"))

        # Introductory Speech on Application startup
        self.speak("Welcome to Tic Tac Toe.")
        self.speak("press control C for Computer mode and control H for Human mode")

    # Reset Board Function
    def resetBoard(self):

        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)

        self.pushButton.setText('')
        self.pushButton_2.setText('')
        self.pushButton_3.setText('')
        self.pushButton_4.setText('')
        self.pushButton_5.setText('')
        self.pushButton_6.setText('')
        self.pushButton_7.setText('')
        self.pushButton_8.setText('')
        self.pushButton_9.setText('')

        self.speak("Board has been reset")

    # Button Click Function
    def btnClk(self, pos):

        '''
        mode H => Human Mode
        mode C => Computer Mode
        :param pos:
        :return:
        '''

        global plyFlag, mode
        mark = ' '

        if mode == 'H':
            if plyFlag % 2 == 0:
                mark = 'X'
            else:
                mark = 'O'

            if pos == 1:
                self.pushButton.setText(mark)
                self.pushButton.setEnabled(False)
            elif pos == 2:
                self.pushButton_2.setText(mark)
                self.pushButton_2.setEnabled(False)
            elif pos == 3:
                self.pushButton_3.setText(mark)
                self.pushButton_3.setEnabled(False)
            elif pos == 4:
                self.pushButton_4.setText(mark)
                self.pushButton_4.setEnabled(False)
            elif pos == 5:
                self.pushButton_5.setText(mark)
                self.pushButton_5.setEnabled(False)
            elif pos == 6:
                self.pushButton_6.setText(mark)
                self.pushButton_6.setEnabled(False)
            elif pos == 7:
                self.pushButton_7.setText(mark)
                self.pushButton_7.setEnabled(False)
            elif pos == 8:
                self.pushButton_8.setText(mark)
                self.pushButton_8.setEnabled(False)
            elif pos == 9:
                self.pushButton_9.setText(mark)
                self.pushButton_9.setEnabled(False)

            plyFlag += 1
            self.chkWin()
            self.chkDraw()

        elif mode == 'C':
            mark = 'X'
            if pos == 1:
                self.pushButton.setText(mark)
                self.pushButton.setEnabled(False)
            elif pos == 2:
                self.pushButton_2.setText(mark)
                self.pushButton_2.setEnabled(False)
            elif pos == 3:
                self.pushButton_3.setText(mark)
                self.pushButton_3.setEnabled(False)
            elif pos == 4:
                self.pushButton_4.setText(mark)
                self.pushButton_4.setEnabled(False)
            elif pos == 5:
                self.pushButton_5.setText(mark)
                self.pushButton_5.setEnabled(False)
            elif pos == 6:
                self.pushButton_6.setText(mark)
                self.pushButton_6.setEnabled(False)
            elif pos == 7:
                self.pushButton_7.setText(mark)
                self.pushButton_7.setEnabled(False)
            elif pos == 8:
                self.pushButton_8.setText(mark)
                self.pushButton_8.setEnabled(False)
            elif pos == 9:
                self.pushButton_9.setText(mark)
                self.pushButton_9.setEnabled(False)

            move = self.compMove()

            if move == 1:
                self.pushButton.setText('O')
            elif move == 2:
                self.pushButton_2.setText('O')
            elif move == 3:
                self.pushButton_3.setText('O')
            elif move == 4:
                self.pushButton_4.setText('O')
            elif move == 5:
                self.pushButton_5.setText('O')
            elif move == 6:
                self.pushButton_6.setText('O')
            elif move == 7:
                self.pushButton_7.setText('O')
            elif move == 8:
                self.pushButton_8.setText('O')
            elif move == 9:
                self.pushButton_9.setText('O')

            self.chkWin()
            self.chkDraw()

    # This function checks if one of X or O is victorious
    def chkWin(self):

        global plyScr1, plyScr2, win
        winner = ' '
        win = True

        if self.pushButton.text() == self.pushButton_2.text() and self.pushButton_2.text() == self.pushButton_3.text():
            winner = self.pushButton.text()
        elif self.pushButton_4.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_6.text():
            winner = self.pushButton_4.text()
        elif self.pushButton_7.text() == self.pushButton_8.text() and self.pushButton_8.text() == self.pushButton_9.text():
            winner = self.pushButton_7.text()
        elif self.pushButton.text() == self.pushButton_4.text() and self.pushButton_4.text() == self.pushButton_7.text():
            winner = self.pushButton.text()
        elif self.pushButton_2.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_8.text():
            winner = self.pushButton_2.text()
        elif self.pushButton_3.text() == self.pushButton_6.text() and self.pushButton_6.text() == self.pushButton_9.text():
            winner = self.pushButton_3.text()
        elif self.pushButton.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_9.text():
            winner = self.pushButton.text()
        elif self.pushButton_3.text() == self.pushButton_5.text() and self.pushButton_5.text() == self.pushButton_7.text():
            winner = self.pushButton_3.text()
        else:
            win = False

        if winner == 'X':
            plyScr1 += 1
            self.label.setText(f"Player X: {plyScr1}")
            self.speak("Player X is victorious")
            self.resetBoard()
        elif winner == 'O':
            plyScr2 += 1
            self.label_2.setText(f"Player O: {plyScr2}")
            self.speak("Player O is victorious")
            self.resetBoard()

    # This Function checks if the board is draw
    def chkDraw(self):

        global win

        if win:
            pass
        else:
            if self.pushButton.text() != "" and self.pushButton_2.text() != "" and self.pushButton_3.text() != "" and self.pushButton_4.text() != "" and self.pushButton_5.text() != "" and self.pushButton_6.text() != "" and self.pushButton_7.text() != "" and self.pushButton_8.text() != "" and self.pushButton_9.text() != "":
                self.speak("The match is draw")
                self.resetBoard()
            else:
                pass

    # This Functions Resets the Score
    def resetScore(self):
        global plyScr1, plyScr2

        plyScr1 = 0
        plyScr2 = 0

        self.label_2.setText(f"Player O: {plyScr2}")
        self.label.setText(f"Player X: {plyScr1}")

        self.speak("Score has been reset to zero")

    # Main Function for Human Mode
    def human(self):

        global mode
        mode = 'H'

        self.speak("Human Mode Activated")

        global plyScr1, plyScr2

        plyScr1 = 0
        plyScr2 = 0

        self.label_2.setText(f"Player O: {plyScr2}")
        self.label.setText(f"Player X: {plyScr1}")

        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)

    # Main Function for Computer Mode
    def comp(self):
        global mode, click, board
        mode = 'C'

        global plyScr1, plyScr2

        plyScr1 = 0
        plyScr2 = 0

        self.label_2.setText(f"Player O: {plyScr2}")
        self.label.setText(f"Player X: {plyScr1}")

        self.speak("Computer Mode Activated")

        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)

    # Algorithm for the Tic Tac Toe Ai
    def compMove(self):

        '''
        Steps:
        1. If there is a winning move take it.
        2. If the player has a possible winning move on their next turn move into that position.
        3. Take any one of the corners. If more than one is available randomly decide.
        4. Take the center position.
        5. Take one of the edges. If more than one is available randomly decide.
        6. If no move is possible the game is a tie.
        :return: move
        '''

        global board

        board[1] = self.pushButton.text()
        board[2] = self.pushButton_2.text()
        board[3] = self.pushButton_3.text()
        board[4] = self.pushButton_4.text()
        board[5] = self.pushButton_5.text()
        board[6] = self.pushButton_6.text()
        board[7] = self.pushButton_7.text()
        board[8] = self.pushButton_8.text()
        board[9] = self.pushButton_9.text()
        # print(board)

        possibleMoves = []
        if self.pushButton.text() == '':
            possibleMoves.append(1)
        if self.pushButton_2.text() == '':
            possibleMoves.append(2)
        if self.pushButton_3.text() == '':
            possibleMoves.append(3)
        if self.pushButton_4.text() == '':
            possibleMoves.append(4)
        if self.pushButton_5.text() == '':
            possibleMoves.append(5)
        if self.pushButton_6.text() == '':
            possibleMoves.append(6)
        if self.pushButton_7.text() == '':
            possibleMoves.append(7)
        if self.pushButton_8.text() == '':
            possibleMoves.append(8)
        if self.pushButton_9.text() == '':
            possibleMoves.append(9)
        # print(possibleMoves)
        move = 0

        # Check for possible winning move to take or to block opponents winning move
        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = board[:]
                boardCopy[i] = let
                if self.isWinner(boardCopy, let):
                    move = i
                    return move

        # Try to take the center
        if 5 in possibleMoves:
            move = 5
            return move

        # Try to take one of the corners
        cornersOpen = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = self.selectRandom(cornersOpen)
            return move

        # Take any edge
        edgesOpen = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move = self.selectRandom(edgesOpen)
            return move

    # Selecting Random Button
    def selectRandom(self, li):
        import random
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]

    # Check if there is a inner in the board list
    def isWinner(self, bo, le):
        # Given a board and a player’s letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don’t have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    # Main Function for Credits
    def credits(self):
        self.speak("Developed on 29th May 2020, by Ansh Gaikwad")

    # Main Function for Instructions
    def instructions(self):
        msg = QMessageBox()
        msg.setWindowTitle("Instructions")
        msg.setText("Understood?")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("Check out the Details!")
        msg.setDetailedText(
            "SHORTCUT KEYS => Ctrl+C: Computer Mode, Ctrl+H: Human Mode, I: Instructions, C: Credits, S: Source Code, D: Developer Info")
        self.speak(
            "Press Control C for Computer Mode, Control H for Human Mode, I for Instructions, C for Credits, S for Source Code, D for Developer Info")
        x = msg.exec_()

    # Main Function for Source Code
    def github(self):
        webbrowser.open("https://github.com/AnshGaikwad/Tic-Tac-Toe")

    # Main Function for Developer Info
    def linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/ansh-gaikwad-13814219a/")

    # Speak Function for the Assistant to speak
    def speak(self, text):
        try:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)  # Set index for voices currently 3 voices available
            engine.say(text)
            engine.runAndWait()
        except:
            pass


# Main Loop
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
