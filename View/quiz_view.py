from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QButtonGroup, QProgressBar, QStyleOption, QStyle
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.setObjectName("quizScreen")
        
        main_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.question_label = QLabel("", self)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setObjectName('questionLabel')
        
        self.score_label =  QLabel("0", self)
        self.score_label.setObjectName('scoreLabel')
        self.header_layout.addWidget(self.question_label)
        self.header_layout.addWidget(self.score_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")
       
        self.answer_layout = QVBoxLayout()
        self.button_group = QButtonGroup()
        self.radio_buttons = []

        for _ in range(4):
            rb = QRadioButton("")
            self.radio_buttons.append(rb)
            self.button_group.addButton(rb)
            self.answer_layout.addWidget(rb)
       
        self.answer_layout.setSpacing(30)
        
        nav_layout = QHBoxLayout()
        self.nav_prev = QPushButton("Previous")
        self.nav_next = QPushButton("Next")
        nav_layout.addWidget(self.nav_prev)
        nav_layout.addWidget(self.nav_next)
        nav_layout.setSpacing(15)
        
        main_layout.addLayout(self.header_layout)
        main_layout.addWidget(self.progress_bar)
        main_layout.addLayout(self.answer_layout)
        main_layout.addLayout(nav_layout)
        self.setLayout(main_layout)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)

    def update_question(self, question, answers):
        self.question_label.setText(question)
        for rb, text in zip(self.radio_buttons, answers):
            rb.setChecked(False)
            rb.setText(text)

    def update_score(self, score):
        self.score_label.setText(str(score))
