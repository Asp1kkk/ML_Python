class FlashCards():
    def __init__(self):
        self.cards = {}
        self.words = []

    def play(self) -> str:
        '''
        Выдает русские слова из словаря в рандомном порядке, 
        сверяет введенный пользователем перевод с правильным 
        (регистр введенного слова при этом не важен), 
        пока слова в словаре не закончатся. 
        Возвращает строку с количеством правильных ответов/общим количеством 
        слов в словаре (см пример работы). 
        '''

    def add_word(self, russian: str, english: str) -> str:
        if not isinstance(russian, str) or not isinstance(english, str):
             return "Неправильный тип ввода"
        if russian in self.words:
             return "Такое слово уже есть в словаре"
        self.cards[russian] = english
        self.words.append(russian)
        return f"Добавлено слово '{russian}'"

    def delete_word(self, russian: str) -> str:
        if not isinstance(russian, str):
             return "Неправильный тип ввода"
        if russian not in self.words:
             return "Такого слова нет в словаре"
        self.words.remove(russian)
        del self.cards[russian]
        return f"Удалено слово '{russian}'"

if __name__ == "__main__":
	fc = FlashCards()
	print(fc.add_word('груша', 'pear'))
	print(fc.add_word('хурма', 'persimmon'))
	print(fc.add_word('яблоко', 'apple'))
	print(fc.delete_word(123))
	print(fc.words)
	print(fc.cards)
    