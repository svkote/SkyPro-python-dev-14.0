from json import load
from question import Question


def load_questions(filename):
    """Загружает список вопросов-ответов,
    создает список questions экземпляров класса Questions"""
    questions = []

    with open(filename, encoding="utf-8") as file:
        data = load(file)

    for item in data:
        question = item['q']
        diff = int(item['d'])
        right_answer = item['a']
        question = Question(question, diff, right_answer)
        questions.append(question)

    return questions


def get_statistics(questions):
    """Выводится статистика на основе списка questions"""
    user_score = 0
    count_right_answer = 0

    for question in questions:
        if question.is_correct():
            user_score += question.score
            count_right_answer += 1

    return(f"""Вот и всё!
Отвечено на {count_right_answer} вопроса из {len(questions)}
Набрано баллов: {user_score}""")
