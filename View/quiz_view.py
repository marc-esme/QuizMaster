from PyQt5.QtWidgets import QWidget, QLabel, QLayout, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QButtonGroup, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.setStyleSheet("background-color: lightblue; font-size: 24px")
        self.setMinimumSize(800,600)
        
       

        # Main Layout

        main_layout = QVBoxLayout()

        #Prompt layout
        self.header_layout = QHBoxLayout()
        self.question_label = QLabel("What is the capital of France?", self)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.question_label.move(50, 100)
        self.score_label =  QLabel("0", self)
        self.header_layout.addWidget(self.question_label)
        self.header_layout.addWidget(self.score_label)
        
        #Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")
       

        #Answer Layout

        self.answer_layout = QVBoxLayout()
        self.button_group = QButtonGroup()
        self.radio_buttons = []

        for _ in range(4):
            rb = QRadioButton("")
            self.radio_buttons.append(rb)
            self.button_group.addButton(rb)
            self.answer_layout.addWidget(rb)
       
        self.answer_layout.setSpacing(30)
        #Navigation Layout

        nav_layout = QHBoxLayout()

        self.nav_prev = QPushButton("Previous")
        self.nav_next = QPushButton("Next")

        nav_layout.addWidget(self.nav_prev)
        nav_layout.addWidget(self.nav_next)

        nav_layout.setSpacing(15)
        
        # Setting up the layouts
        main_layout.addLayout(self.header_layout)
        main_layout.addWidget(self.progress_bar)
        main_layout.addLayout(self.answer_layout)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)

    def update_question(self, question, answers):
        self.question_label.setText(question)
        for rb, text in zip(self.radio_buttons, answers):
            rb.setChecked(False)
            rb.setText(text)

    def update_score(self, score):
        self.score_label.setText(str(score))