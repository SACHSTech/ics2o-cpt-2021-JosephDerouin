class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "B"),
]


###Adding up correct Answers###
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + correct)