from random import sample

name = input("Введите ваше имя:\n 👉🏻 ")


# - чтение слов из файла
def get_list(filename):
    ready_list = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            ready_list.append(line.replace('\n', ''))
    return ready_list


# - чтение топа игроков history.txt
def get_top(name):
    count = 0
    max_record = 0
    with open('history.txt', encoding='utf-8') as file:
        for line in file:
            line = line.replace('\n', '')
            if name in line:
                count += 1
                max_record = int(line.split()[-1]) if max_record < int(line.split()[-1]) else max_record
    return count, max_record


# - запись в топ игроков. history.txt
def write_top(name, score):
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} - {score}\n')


def game(name):
    words_list = get_list('words.txt')
    score = 0
    for word in words_list:
        shuffle_word = ''.join(sample(word, len(word)))
        answer = input(f'Угадайте слово: {shuffle_word}').lower()
        if answer == word:
            print(f'Верно, {name}! Вы получаете 10 очков.')
            score += 10
        else:
            print(f'Неверно, {name}! Верный ответ – {word}')
    write_top(name, score)
    count, max_record = get_top(name)
    print(f'Всего игр сыграно: {count}')
    print(f'Максимальный рекорд: {max_record}')


game(name)
