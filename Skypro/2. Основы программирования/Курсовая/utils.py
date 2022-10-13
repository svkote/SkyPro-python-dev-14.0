from requests import get
from random import choice
from basic_word import BasicWord


def load_random_word():
    """Получает список слов с внешнего ресурса. Выбирает случайное слово.
    Создает экземпляр класса `BasicWord` и возвращает его."""
    # получаем список слов с внешнего ресурса
    response = get('https://www.jsonkeeper.com/b/WMNC')
    response_json = response.json()
    # выбираем случайное слово
    choice_word = choice(response_json)
    # создаем экземпляр класса `BasicWord`
    original_word = choice_word['word']
    right_words = choice_word['subwords']
    basic_word = BasicWord(original_word, right_words)
    # возвращаем этот экземпляр.
    return basic_word


