from PyQt5.QtWidgets import QMessageBox

START_PAGE = 0
QUIZ_PAGE = 1
RESULT_PAGE = 2

class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.quiz_view.nav_next.clicked.connect(self.next_question) 
        self.view.quiz_view.nav_prev.clicked.connect(self.prev_question)
        self.view.quiz_view.nav_prev.setEnabled(False)
        
        self.view.start_view.start_button.clicked.connect(self.start_quiz)
        self.view.result_view.restart_button.clicked.connect(self.restart)

        self.view.quiz_view.progress_bar.setMaximum(len(self.model.questions))
        
    def start_quiz(self):
        self.view.stack.setCurrentIndex(QUIZ_PAGE)
        self.update_view()
    
    def restart(self):
        self.model.current_index = 0
        self.model.score = 0
        self.model.answered_questions = set()
        self.update_view()
        self.view.stack.setCurrentIndex(START_PAGE)

    def update_view(self):
        current = self.model.get_current_question()
        self.view.quiz_view.update_question(current["question"], current["answers"])
        self.view.quiz_view.progress_bar.setValue(self.model.current_index)
        self.view.quiz_view.update_score(self.model.score)


    def next_question(self):
        selected_button = self.view.quiz_view.button_group.checkedButton()
        if not selected_button :
            QMessageBox.warning(self.view, "Error", "You must choose one answer")
            return 
        answer = selected_button.text()
        if self.model.current_index not in self.model.answered_questions:
            
            is_correct = self.model.check_answer(answer)
            self.model.answered_questions.add(self.model.current_index)
            if self.model.current_index+1 < len(self.model.questions):
                self.model.current_index += 1
                self.update_view()
            else:
                self.update_view()
                self.show_result()
                self.view.quiz_view.nav_prev.setEnabled(True)

    def prev_question(self):
        if self.model.current_index > 0:
            self.model.current_index -= 1
            self.update_view()
            for button in self.view.quiz_view.radio_buttons:
                button.setEnabled(False)

    def show_result(self):
        # fetch score from model attribute
        score = self.model.score
    
        # update score display using view method
        self.view.result_view.result_label.setText(f"Final Score : {score}")
    
        # update visible layer in the stack
        self.view.stack.setCurrentIndex(RESULT_PAGE)
