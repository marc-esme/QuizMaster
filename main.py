import sys
# Main class for the PyQt5 application
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
# Import the main application window
from View.quiz_view import QuizView
from Controller.quiz_controller import QuizController
from Model.quiz_model import QuizModel

app = QApplication(sys.argv) # Creates the application
app.setWindowIcon(QIcon("Resources/quizicon.png"))
#setup app
model = QuizModel()
window = QuizView() # Creates the window
controller = QuizController(model, window)

#launch the app
window.show() # Displays the window
sys.exit(app.exec_()) # Starts the application loop and exits cleanly