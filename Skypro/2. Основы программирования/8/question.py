class Question:
    """Класс, отвечающий за вопросы. Содержит поля:
    – текст вопроса
    – сложность вопроса
    – верный вариант ответа
    – задан ли вопрос (по умолчанию False)
    – ответ пользователя (по умолчанию None)
    – баллы за вопрос (вычисляется в момент инициализации)"""

    def __init__(self, question, diff, right_answer):
        self.question = question  # текст вопроса
        self.diff = diff  # сложность вопроса
        self.right_answer = right_answer  # верный вариант ответа

        self.is_asked = False  # задан ли вопрос (по умолчанию False)
        self.user_answer = None  # ответ пользователя (по умолчанию None)
        self.score = self.diff * 10  # баллы за вопрос (вычисляется в момент инициализации)

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.right_answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question}\nСложность: {self.diff}/5"

    def build_feedback(self):
        """Возвращает:
        Если ответ верный: Ответ верный, получено __ баллов
        Если ответ неверный: Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ {self.right_answer}"
