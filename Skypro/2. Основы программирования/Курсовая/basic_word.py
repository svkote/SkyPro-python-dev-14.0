class BasicWord:
    def __init__(self, original_word, right_words):
        self.original_word = original_word
        self.right_words = right_words

    # проверку введенного слова в списке допустимых подслов (вернет bool),
    def check_word(self, user_word):
        return user_word in self.right_words

    # подсчет количества подслов (вернет int).
    def count_right_words(self):
        return len(self.right_words)

    def __repr__(self):
        return 'Исходное слово и набор допустимых слов'
