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


if __name__ == '__main__':
    main()


