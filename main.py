#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel)

class typeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initailizeUI()
    
    def initailizeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Taccs Typer')
        self.practiceUI()

        self.show()
    
    def practiceUI(self):
        self.resopnse_label = QLabel(self)
        self.resopnse_label.setText("No good")

        self.exerciseLine = QLineEdit(self)
        self.exerciseLine.move(50, 50)
        # Test text
        self.exerciseLine.setText("Hello")
        # self.exerciseLine.setEnabled(False)

        self.textInput = QLineEdit(self)
        self.textInput.move(50, 100)
        self.textInput.textChanged.connect(self.inputHandler)
    
    def inputHandler(self):
        try:
            if self.textInput.text()[-1] == " ":
                # Debug stuff
                print("new word")
                wanted_word = self.exerciseLine.text()
                my_word = self.textInput.text().split()[-1]
                print(wanted_word, my_word)

                # 
                if wanted_word == my_word:
                    self.resopnse_label.setText("Good")
                else:
                    self.resopnse_label.setText("no good")
        except IndexError:
            pass
        

    



##########################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = typeWindow()
    sys.exit(app.exec_())
