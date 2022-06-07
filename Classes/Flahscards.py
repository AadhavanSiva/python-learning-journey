class Flashcard:
    answer: object

    def __init__(self, number, question, answer):
        self.number = number
        self.question = question
        self.answer = answer

    def print(self):
        print("The flashcard's number is ", self.number)
        print("The question is " + self.question)
        print("The answer is " + self.answer )

    def validate(self, userAnswer):
        return userAnswer == self.answer
        # if userAnswer == self.answer:
        #     return True
        # else:
        #     return False


flash1 = Flashcard(1,"who owns microsoft", "Bill Gates")
flash2 = Flashcard(2,"Who owns tesla ", "Elon Musk")
userAnswer = "Bill Gates"   #input("what is the answer to " + flash1.question)
status = flash1.validate(userAnswer)
if status:
    print("correct it is " + userAnswer)
else:
    print("wrong it is not " + userAnswer)
#flash1.print()
#flash2.validate()
