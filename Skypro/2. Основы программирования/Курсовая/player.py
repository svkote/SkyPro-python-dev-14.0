class Player:
    def __init__(self, player_name):
        self.player_name = player_name  # имя пользователя
        self.player_words = []  # использованные слова пользователя

    def get_count_words(self) -> int:
        """Получение количества использованных слов (возвращает int)"""
        return len(self.player_words)

    def append_words(self, word):
        """Добавление слова в использованные слова (ничего не возвращает)"""
        self.player_words.append(word)

    def check_word(self, word) -> bool:
        """Проверка использования данного слова до этого (возвращает bool)"""
        return word in self.player_words

    def __repr__(self):
        return f"Player {self.player_name} - {self.player_words}"
