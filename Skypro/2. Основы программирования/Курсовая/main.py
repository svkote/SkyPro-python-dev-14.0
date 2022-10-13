from player import Player
from utils import load_random_word


def main():
    # Получаем у пользователя его имя.
    player_name = input('Ввведите имя игрока:\n➡️')

    # Создаем экземпляр класса Player с нужным именем.
    player = Player(player_name)

    # Здороваемся с пользователем
    print(f'Привет, {player.player_name}')
    basic_word = load_random_word()

    # Выводим значение слова из экземпляра, который получили ранее из `load_random_word`.
    print(f'Составьте {len(basic_word.right_words)} слов из слова {basic_word.original_word}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')

    # пока количество угаданных слов не сравняется с количеством слов, которые можно составить
    while player.get_count_words() != basic_word.count_right_words():
        answer = input('➡️').lower()

        # Если слово stop или стоп, то игра прекращается.
        if answer in ['stop', 'стоп']:
            break

        # Если слово короче 3 букв – это неудачное слово.
        if len(answer) < 3:
            print('Слишком короткое слово')
            continue

        # Если слова нет в списке допустимых у BasicWord – это неудачное слово.
        if basic_word.check_word(answer):
            print('Неверно')
            continue

        # Если слово уже было угадано пользователем (Player) – это неудачное слово.
        if player.check_word(answer):
            print('Уже использовано')
            continue

        # Если все проверки выше пройдены, то слово хорошее,
        # его нужно добавить слово в список использованных слов класса Player и вывести оповещение об этом пользователю:
        player.append_words(answer)
        print('Верно')

    print(f'Игра завершена, вы угадали {player.get_count_words()} слов!')


if __name__ == '__main__':
    main()
