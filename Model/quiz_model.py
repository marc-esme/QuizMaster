import json

class QuizModel():

    def __init__(self,json_file="Resources/questions.json"):
        self.questions = self.load_questions(json_file)
        self.current_index = 0
        self.score = 0
        self.answered_questions = set() #keep tracks of answered questions


    def get_current_question(self):
        return self.questions[self.current_index]
    
    def check_answer(self, answer):
        if answer == self.get_current_question().get("correct"):
            self.score +=1
            return True
        return False
    
    def load_questions(self, json_file):
        with open(json_file, "r") as question_bank:
            return json.load(question_bank)


## DEBUG 

model = QuizModel()
print(model.get_current_question())