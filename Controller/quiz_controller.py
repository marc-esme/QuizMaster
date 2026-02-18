from PyQt5.QtWidgets import QMessageBox

class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.nav_next.clicked.connect(self.next_question)
    
    
    def next_question(self):
        selected_button = self.view.button_group.checkedButton()
        if not selected_button:
            QMessageBox.warning( self.view, "Warning", "You must select a choice to continue.")
            return
        
        answer = selected_button.text()

        is_correct = self.model.check_answer(answer)

        if is_correct:
            QMessageBox.information( self.view, "Good Job", "You have the correct answer.")

        else:
             QMessageBox.information( self.view, "Too bad", "You have the wrong answer.")

        print(f"Current score: {self.model.score}")