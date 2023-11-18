class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question = Question("Hello", "World")
print(question.question)