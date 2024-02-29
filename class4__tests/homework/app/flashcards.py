import re

class FlashCards():
    def __init__(self):
        self.engs = []
        self.words = []

    def play(self) -> str:
        if not len(self.words):
            return "В словаре нет слов"
        rightAns = 0
        for i in range(len(self.words)):
            guess = input(f"{self.words[i]}\n")
            if guess.lower() == self.engs[i]:
                 rightAns += 1
        return f"Готово! Правильно {rightAns} из {len(self.words)}"

    def add_word(self, russian: str, english: str) -> str:
        if not isinstance(russian, str) or not isinstance(english, str):
             return "Неправильный тип ввода"
        if russian.strip() == '' or english.strip() == '':
            return "Введите данные"
        if re.search('[a-zA-Z]', russian):
            return "Первое слово должно быть русским"
        if russian in self.words:
             return "Такое слово уже есть в словаре"
        self.engs.append(english)
        self.words.append(russian)
        return f"Добавлено слово '{russian}'"

    def delete_word(self, russian: str) -> str:
        if not isinstance(russian, str):
             return "Неправильный тип ввода"
        if russian.strip() == '':
            return "Введите данные"
        if russian not in self.words:
             return "Такого слова нет в словаре"
        self.engs.remove(self.engs[self.words.index(russian)])
        self.words.remove(russian)
        return f"Удалено слово '{russian}'"