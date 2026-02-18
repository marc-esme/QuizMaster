class QuizModel():

    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "answers": ["Paris", "Lyon", "Marseille", "Bordeaux"],
                "correct": "Paris",
            },
             {
                "question": "What is the capital of Australia?",
                "answers": ["Sydney", "Adelaide", "Perth", "Canberra"],
                "correct": "Canberra",
            }
        ]
        self.current_index = 0
        self.score = 0


    def get_current_question(self):
        return self.questions[self.current_index]
    
    def check_answer(self, answer):
        if answer == self.get_current_question().get("correct"):
            self.score +=1
            return True
        return False