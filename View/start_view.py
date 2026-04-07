from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QStyleOption, QStyle
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
class StartView(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("startScreen")
        
        layout = QVBoxLayout()
        self.title = QLabel("Welcome to the Quiz")
        self.title.setAlignment(Qt.AlignCenter)
        self.start_button = QPushButton("Start")
        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def paintEvent(self, event):
        """Required to make QSS background-image/border-image work on custom QWidget subclasses."""
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
