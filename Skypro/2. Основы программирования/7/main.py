from functions import *


def main():
    student_pk = int(input("Введите номер студента:\n👉🏻 "))
    student = get_student_by_pk(student_pk)
    if student:
        print(f"Студент {student['full_name']}")
        print(f"Знает {', '.join(student['skills'])}")
    else:
        print("У нас нет такого студента")
        quit()
    prof_title = input(f"Выберите специальность для оценки студента {student['full_name']}:\n👉🏻 ").title()
    profession = get_profession_by_title(prof_title)
    if profession:
        dict_fitness = check_fitness(student, profession)
        print(f"Пригодность {dict_fitness['fit_percent']}%")
        print(f"{student['full_name']} знает {', '.join(dict_fitness['has'])}")
        print(f"{student['full_name']} не знает {', '.join(dict_fitness['lacks'])}")
    else:
        print("У нас нет такой специальности")
        quit()


if __name__ == '__main__':
    main()
