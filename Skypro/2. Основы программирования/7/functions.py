import json


def load_students():
    """Загружает список студентов из файла"""
    with open('students.json', encoding='utf-8') as file:
        students = json.load(file)
    return students


def load_professions():
    """Загружает список профессий из файла"""
    with open('professions.json', encoding='utf-8') as file:
        professions = json.load(file)
    return professions


def get_student_by_pk(pk):
    """Получает словарь с данными студента по его pk
    Формат: {'pk': 1, 'full_name': 'Jane Snake', 'skills': ['Python', 'Go', 'Linux']}"""
    students = load_students()
    for student in students:
        if student['pk'] == pk:
            return student
    return None


def get_profession_by_title(title):
    """Получает словарь с инфо о профе по названию
    Формат: {'pk': 1, 'title': 'Backend', 'skills': ['Python', 'Linux', 'Docker', 'SQL', 'Flask']}"""
    professions = load_professions()
    for profession in professions:
        if profession['title'] == title:
            return profession
    return None


def check_fitness(student, profession):
    """Возвращает словарь, получив студента и его профессию
    Формат: {'has': ['Python', 'Linux'], 'lacks': ['SQL', 'Docker', 'Flask'], 'fit_percent': 40}"""
    skill_student = set(student['skills'])
    skill_prof = set(profession['skills'])
    has = list(skill_student.intersection(skill_prof))
    lacks = list(skill_prof.difference(skill_student))
    fit_percent = int(len(has) / len(skill_prof) * 100)
    dict_fitness = {"has": has, "lacks": lacks, "fit_percent": fit_percent}
    return dict_fitness


print(get_student_by_pk(pk=1))
stud = get_student_by_pk(pk=1)
print(get_profession_by_title('Backend'))
prof = get_profession_by_title('Backend')
print(check_fitness(stud, prof))
