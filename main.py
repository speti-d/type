#!/usr/bin/env python3
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt

class typeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initailizeUI()
    
    def initailizeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Taccs Typer')
        self.practiceUI()

        self.show()
    
    def practiceUI(self):
        self.resopnse_label = QtWidgets.QLabel(self)
        self.resopnse_label.setText("No good")

        self.exerciseLine = QtWidgets.QLineEdit(self)
        self.exerciseLine.move(50, 50)
        self.exerciseLine.setText("Hello")

        self.textInput = typeLineEdit(self)
        self.textInput.move(50, 100)
        
class typeLineEdit(QtWidgets.QLineEdit):
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(typeLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Space:
            print("Space was pressed")




##########################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = typeWindow()
    sys.exit(app.exec_())
