class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input("Q.{} {} (True or False) ".format(self.question_no, current_question.text))
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print("Your score is {}/{}".format(self.score, self.question_no))
        print("The correct answer was {}".format(c_answer))
        print()
