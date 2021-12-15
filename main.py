# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pyqtgraph as pg
from datetime import datetime
import random
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMessageBox


def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)

        self.exercise_timer = QtCore.QTimer()
        self.exercise_timer.timeout.connect(self.updateTimerClock)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout.addWidget(self.label_username)

        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")

        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton_username = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_username.setObjectName("pushButton_username")
        self.pushButton_username.clicked.connect(self.enterUsername)
        self.verticalLayout_2.addWidget(self.pushButton_username)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.stats_label = QtWidgets.QLabel(self.centralwidget)
        self.stats_label.setObjectName("stats_label")
        self.gridLayout.addWidget(self.stats_label, 0, 0, 1, 1)

        self.stats_label2 = QtWidgets.QLabel(self.centralwidget)
        self.stats_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.stats_label2.setObjectName("stats_label2")
        self.gridLayout.addWidget(self.stats_label2, 1, 0, 1, 1)

        self.pushButton_graph = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_graph.setObjectName("pushButton_graph")
        self.pushButton_graph.setText("Show history")
        self.pushButton_graph.setDisabled(True)
        self.pushButton_graph.clicked.connect(self.showpopup)
        self.gridLayout.addWidget(self.pushButton_graph, 2, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_exercise = QtWidgets.QLabel(self.centralwidget)
        self.label_exercise.setStyleSheet("background-color: white;")
        self.label_exercise.setAlignment(QtCore.Qt.AlignCenter)
        self.label_exercise.setFont(QtGui.QFont('Arial', 15))
        self.label_exercise.setObjectName("label_exercise")
        self.verticalLayout.addWidget(self.label_exercise)


        self.lineEdit_exercise = typeLineEdit(self.centralwidget)
        self.lineEdit_exercise.setObjectName("lineEdit_exercise")
        self.lineEdit_exercise.setDisabled(True)
        self.verticalLayout.addWidget(self.lineEdit_exercise)

        self.pushButton_exercise = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exercise.setObjectName("pushButton_exercise")
        self.pushButton_exercise.clicked.connect(self.startExercise)
        self.pushButton_exercise.setDisabled(True)
        self.verticalLayout.addWidget(self.pushButton_exercise)

        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "type"))
        self.label_username.setText(_translate("MainWindow", "Username:"))
        self.pushButton_username.setText(_translate("MainWindow", "Enter"))
        self.stats_label.setText(_translate("MainWindow", "Stats go here"))
        self.label_exercise.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_exercise.setText(_translate("MainWindow", "Start Exercise"))

    def showpopup(self):
        print("here")
        pop = graphWindow()
        pop.show()

    def startExercise(self):
        self.pushButton_exercise.setDisabled(True)
        self.lineEdit_exercise.setDisabled(False)
        self.timeleft = 60
        # the time the exercise is meant to take
        self.exercise_timer.start(1000)  # timer ticking once every second

        print("exercise started")

        self.currentword = 0
        self.exercise_wordlist = []

        self.getWords(10)
        self.updateDisplay()

        self.stats_label.setText(f"Time left: {self.timeleft}")
        self.lineEdit_exercise.clear()
        self.lineEdit_exercise.setFocus()


    def enterUsername(self):
        if len(self.lineEdit_username.text()) >= 4:
            self.pushButton_exercise.setDisabled(False)
            self.lineEdit_username.setDisabled(True)
            self.pushButton_graph.setDisabled(False)

    def endExercise(self):
        print("exercise ended")
        self.exercise_timer.stop()
        good_words = 0
        self.lineEdit_exercise.setDisabled(True)

        good_words = 0
        input_list = self.lineEdit_exercise.text().split(" ")

        for index in range(min(len(input_list), len(self.exercise_wordlist))):
            if self.exercise_wordlist[index] == input_list[index]:
                good_words += 1

        self.scoreWrite(good_words)
        self.stats_label2.setText(f"WPM: {good_words}")
        print(f"WPM {good_words}")
        self.pushButton_exercise.setDisabled(False)


    def updateDisplay(self, start=0, end=10):
        if start < 0:
            start = 0
        exercise_text = ""
        # exercise_text = " ".join([word for word in self.exercise_wordlist])
        for i in range(start, end):
            exercise_text += self.exercise_wordlist[i] + " "
        self.label_exercise.setText(exercise_text)


    def scoreWrite(self, score):
        if self.lineEdit_username.text == "":
            return None
        with open("scores.txt", 'r') as f1:
            lines = f1.readlines()
        with open("scores.txt", 'w') as out:
            for line in lines:
                out.write(line)
            out.write(f"{self.lineEdit_username.text()};{score};{datetime.now()}\n")

    def getWords(self, x):
        with open("words.txt", "r") as f1:
            wordlist = f1.readline().split(";")
            for n in range(x):
                self.exercise_wordlist.append(random.choice(wordlist))


    def updateTimerClock(self):
        self.timeleft -= 1
        self.stats_label.setText(f"Time left: {self.timeleft}")
        if self.timeleft == 0:
            self.endExercise()


    def onSpaceHit(self):
        good_words = 0
        input_list = self.lineEdit_exercise.text().split(" ")
        self.currentword = len(input_list)
        self.getWords(1)

        self.updateDisplay(self.currentword - 1, self.currentword + 9)

        for index in range(min(len(input_list), len(self.exercise_wordlist))):
            if self.exercise_wordlist[index] == input_list[index]:
                good_words += 1

        self.stats_label2.setText(f"WPM: {good_words}")
        # TODO: Rename this and make it edit the displayed text
        # in the exercise TextEdit


class typeLineEdit(QtWidgets.QLineEdit):
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(typeLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Space:
            # print("Space was pressed")
            ui.onSpaceHit()

class graphWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        with open("scores.txt", 'r') as f1:
            lines = f1.readlines()

        yourscores = [(int(line.split(';')[1]), line.split(';')[2].strip())
                      for line in lines if line.split(';')[0] == ui.lineEdit_username.text()]

        print(yourscores)
        yourscores = sorted(yourscores, key=lambda i: i[1])
        y = [num for (num, whatever) in yourscores]


        x = [to_integer(datetime.strptime(date[:-7], "%Y-%m-%d %H:%M:%S")) for (whatever, date) in yourscores]
        print(x)

        plt = pg.plot()

        plt.showGrid(x=True, y=True)

        plt.addLegend()

        plt.setLabel('left', 'wpm', units='y')

        plt.setLabel('bottom', 'date', units='s')

        plt.setXRange(20000000, 20220000)

        plt.setYRange(0, 200)

        plt.setWindowTitle("History")

        line1 = plt.plot(x, y, pen='g', symbol='x', symbolPen='g',
                         symbolBrush=0.2, name='green')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
