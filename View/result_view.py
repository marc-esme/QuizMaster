from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QStyleOption, QStyle
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
class ResultView(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("resultScreen")
        
        layout = QVBoxLayout()
        self.result_label = QLabel("Score: 0")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.restart_button = QPushButton("Restart")
        layout.addWidget(self.result_label)
        layout.addWidget(self.restart_button)
        self.setLayout(layout)

    def paintEvent(self, event):
        """Required to make QSS background-image/border-image work on custom QWidget subclasses."""
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
