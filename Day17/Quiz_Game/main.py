from question_model import Question
from data import question_data

question_bank = []

for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)


class QuizBrain:

    def __init__(self, question_no):
        self.question_no = question_no
