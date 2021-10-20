#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit

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
        self.textInput = QTextEdit(self)
        self.textInput.resize(200, 200)
        self.textInput.move(20, 20)




##########################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = typeWindow()
    sys.exit(app.exec_())
