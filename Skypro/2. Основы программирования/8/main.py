from functions import load_questions, get_statistics

filename = "questions.json"


def main():
    questions = load_questions(filename)

    for question in questions:
        print(question.build_question())
        question.user_answer = input("Введите ответ: \n👉🏻 ")
        print(question.build_feedback())

    print(get_statistics(questions))


if __name__ == '__main__':
    main()
