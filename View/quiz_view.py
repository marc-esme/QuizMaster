from PyQt5.QtWidgets import QWidget, QLabel, QLayout, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.setStyleSheet("background-color: lightblue; font-size: 24px")
        self.setMinimumSize(800,600)
        self.question_label = QLabel("What is the capital of France?", self)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.question_label.move(50, 100)

        # Main Layout

        main_layout = QVBoxLayout()


        #Answer Layout

        answer_layout = QVBoxLayout()
        answer_1 = QRadioButton("Paris")
        answer_2 = QRadioButton("Lyon")
        answer_3 = QRadioButton("Marseille")
        answer_4 = QRadioButton("Bordeaux")
        
        #Button group
        self.button_group = QButtonGroup()
        self.button_group.addButton(answer_1)
        self.button_group.addButton(answer_2)
        self.button_group.addButton(answer_3)
        self.button_group.addButton(answer_4)
        
        answer_layout.addWidget(answer_1)
        answer_layout.addWidget(answer_2)
        answer_layout.addWidget(answer_3)
        answer_layout.addWidget(answer_4)

        answer_layout.setSpacing(30)
        #Navigation Layout

        nav_layout = QHBoxLayout()

        self.nav_prev = QPushButton("Previous")
        self.nav_next = QPushButton("Next")

        nav_layout.addWidget(self.nav_prev)
        nav_layout.addWidget(self.nav_next)

        nav_layout.setSpacing(15)
        # Setting up the layouts
        main_layout.addWidget(self.question_label)
        main_layout.addLayout(answer_layout)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)