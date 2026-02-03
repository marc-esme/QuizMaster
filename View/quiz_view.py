from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.setStyleSheet("background-color: lightblue;")
        self.setMinimumSize(800,600)
       