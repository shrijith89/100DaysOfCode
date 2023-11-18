class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        input("Q.{} {} (True or False)".format(self.question_no, current_question.text))

