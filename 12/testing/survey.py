class survey:
    """Собирает ответы на вопрос"""
    def __init__(self, quest):
        self.question = quest
        self.answers = []

    def show_question(self):
        print(self.question)

    def save_answer(self, answer):
        self.answers.append(answer)

    def show_results(self):
        print("Survey results:")
        for answer in self.answers:
            print(f'- {answer}')