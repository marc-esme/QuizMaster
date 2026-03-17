from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
class StartView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.title = QLabel("Welcome to the Quiz")
        self.start_button = QPushButton("Start")
        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        self.setLayout (layout)