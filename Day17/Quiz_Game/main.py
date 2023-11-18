from question_model import Question
from data import question_data

question_bank = []

for data in question_data:
    question = Question(data.get("text"), data.get("answer"))
    question_bank.append(question)