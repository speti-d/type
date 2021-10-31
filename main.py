#!/usr/bin/env python3
import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore, Qt

class typeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initailizeUI()
    
    def initailizeUI(self):
        # Place for things like the layoutmanager 
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Taccs Typer')
        self.practiceUI()

        self.show()
    
    def practiceUI(self):
        # Place for individual widgets

        # QTimer to mesure the 1 minute for the exercise
        self.exercise_timer = QtCore.QTimer()
        self.exercise_timer.timeout.connect(self.endExercise)

        # Label for later use
        self.resopnse_label = QtWidgets.QLabel(self)
        self.resopnse_label.setText("No good")

        # QPushbutton to start the exercise with
        self.start_button = QtWidgets.QPushButton("Start" ,self)
        self.start_button.move(50, 230)
        self.start_button.clicked.connect(self.startExercise)

        # QTextEdit widget to display 
        self.exerciseLine = QtWidgets.QTextEdit(self)
        self.exerciseLine.resize(200, 150)
        self.exerciseLine.move(50, 50)
        self.exerciseLine.setReadOnly(True)

        # The lineEdit into we actually want to type
        self.textInput = typeLineEdit(self)
        self.textInput.move(50, 200)
    
    def startExercise(self):
        self.start_button.setDisabled(True)
        # self.exercise_timer.start(60000) # actual timer for general use
        self.exercise_timer.start(10000) # ten second timer for testing
        print("exercise started")
        exercise_text = ""
        with open("words.txt", 'r') as f1:
            wordlist = f1.readline().split(';')
            for n in range(50):
                exercise_text += random.choice(wordlist) + " "
        self.exerciseLine.setText(exercise_text)
    
    def endExercise(self):
        print("exercise ended")
        self.exercise_timer.stop()
        good_words = 0
        exercise_list = self.exerciseLine.toPlainText().split(' ')
        input_list = self.textInput.text().split(' ')
        for index in range(min(len(input_list), len(exercise_list))):
            if exercise_list[index] == input_list[index]:
                good_words += 1
        print('Good words:', good_words) # Prints to terminal for now
        self.start_button.setDisabled(False)
        # TODO: Connect this to the response label, and calculate wpm
        
class typeLineEdit(QtWidgets.QLineEdit):
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(typeLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Space:
            print("Space was pressed")
            # TODO: Actually check how correct the input is on each spacebar press




##########################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = typeWindow()
    sys.exit(app.exec_())
