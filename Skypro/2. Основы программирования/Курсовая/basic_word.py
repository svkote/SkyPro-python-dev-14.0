class BasicWord:
    def __init__(self, original_word, right_words):
        self.original_word = original_word  # исходное слово
        self.right_words = right_words  # набор допустимых подслов

    def check_word(self, user_word) -> bool:
        """Проверка введенного слова в списке допустимых подслов(вернет bool)"""
        return user_word in self.right_words

    def count_right_words(self) -> int:
        """Подсчет количества подслов(вернет int)"""
        return len(self.right_words)

    def __repr__(self):
        return f'BasicWord {self.original_word} - {self.right_words}'
