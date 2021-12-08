#!/usr/bin/env python3
import sys
from datetime import datetime
import random
from PyQt5 import QtWidgets, QtGui, QtCore, Qt


class typeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initailizeUI()


    def initailizeUI(self):
        # Place for things like the layoutmanager
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Taccs Typer")
        self.setWidgets()

        self.show()


    def setWidgets(self):
        # Place for individual widgets

        # QTimer to mesure the 1 minute for the exercise
        self.exercise_timer = QtCore.QTimer()
        self.exercise_timer.timeout.connect(self.updateTimerClock)

        # Timer label
        self.timer_label = QtWidgets.QLabel(self)
        self.timer_label.setText("Time left:\t")

        # Label for later use
        self.resopnse_label = QtWidgets.QLabel(self)
        self.resopnse_label.setText("WPM: \t\t")
        self.resopnse_label.move(150, 230)

        # QPushbutton to start the exercise with
        self.start_button = QtWidgets.QPushButton("Start", self)
        self.start_button.move(50, 230)
        self.start_button.clicked.connect(self.startExercise)

        # QTextEdit widget to display
        self.exerciseLine = QtWidgets.QTextEdit(self)
        self.exerciseLine.resize(600, 50)
        self.exerciseLine.move(50, 50)
        self.exerciseLine.setFontPointSize(21)
        self.exerciseLine.setReadOnly(True)

        # The lineEdit into we actually want to type
        self.textInput = typeLineEdit(self)
        self.textInput.move(50, 200)

        # Username input
        self.UsernameInput = QtWidgets.QLineEdit(self)
        self.UsernameInput.move(600, 150)
        self.UsernameInput.setInputMask("AAAAaaaaaa")
        self.UsernameInput.setPlaceholderText("Username")


    def startExercise(self):
        self.start_button.setDisabled(True)
        self.textInput.setDisabled(False)
        self.timeleft = 60
        # the time the exercise is meant to take
        self.exercise_timer.start(1000)  # timer ticking once every second

        print("exercise started")

        self.currentword = 0
        self.exercise_wordlist = []

        self.getWords(10)
        self.updateDisplay()

        self.timer_label.setText(f"Time left: {self.timeleft}")
        self.textInput.clear()
        self.textInput.setFocus()


    def endExercise(self):
        print("exercise ended")
        self.exercise_timer.stop()
        good_words = 0
        # self.textInput.setDisabled(True)

        good_words = 0
        input_list = self.textInput.text().split(" ")

        for index in range(min(len(input_list), len(self.exercise_wordlist))):
            if self.exercise_wordlist[index] == input_list[index]:
                good_words += 1

        self.scoreWrite(good_words)
        self.resopnse_label.setText(f"WPM: {good_words}")
        print(f"WPM {good_words}")  
        self.start_button.setDisabled(False)


    def updateDisplay(self, start=0, end=10):
        if start < 0:
            start = 0
        exercise_text = ""
        # exercise_text = " ".join([word for word in self.exercise_wordlist])
        for i in range(start, end):
            exercise_text += self.exercise_wordlist[i] + " "
        self.exerciseLine.setText(exercise_text)


    def scoreWrite(self, score):
        if self.UsernameInput.text == "":
            return None
        with open("scores.txt", 'r') as f1:
            lines  = f1.readlines()
        with open("scores.txt", 'w') as out:
            print("here")
            for line in lines:
                out.write(line)
            out.write(f"{self.UsernameInput.text()};{score};{datetime.now()}\n")

    def getWords(self, x):
        with open("words.txt", "r") as f1:
            wordlist = f1.readline().split(";")
            for n in range(x):
                self.exercise_wordlist.append(random.choice(wordlist))


    def updateTimerClock(self):
        self.timeleft -= 1
        self.timer_label.setText(f"Time left: {self.timeleft}")
        if self.timeleft == 0:
            self.endExercise()


    def onSpaceHit(self):
        good_words = 0
        input_list = self.textInput.text().split(" ")
        self.currentword = len(input_list)
        self.getWords(1)

        self.updateDisplay(self.currentword - 1, self.currentword + 9)

        for index in range(min(len(input_list), len(self.exercise_wordlist))):
            if self.exercise_wordlist[index] == input_list[index]:
                good_words += 1

        self.resopnse_label.setText(f"WPM: {good_words}")
        # TODO: Rename this and make it edit the displayed text
        # in the exercise TextEdit


class typeLineEdit(QtWidgets.QLineEdit):
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(typeLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Space:
            # print("Space was pressed")
            window.onSpaceHit()
            # TODO: Actually check how correct the input is on each spacebar press


##########################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = typeWindow()
    sys.exit(app.exec_())
