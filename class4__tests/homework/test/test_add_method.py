import unittest
from app.flashcards import FlashCards

class Test_add(unittest.TestCase):
	def setUp(self) -> None:
		self.flash = FlashCards()
	
	def test_TypeMismatch_1(self):
		self.assertEqual(self.flash.add_word(123, 321), "Неправильный тип ввода")
	
	def test_TypeMismatch_2(self):
		self.assertEqual(self.flash.add_word(True, False), "Неправильный тип ввода")
	
	def test_Empty_1(self):
		self.assertEqual(self.flash.add_word('', '       '), "Введите данные")

	def test_Empty_2(self):
		self.assertEqual(self.flash.add_word('      ', ''), "Введите данные")

	def test_Already_in(self):
		self.flash.words = ["существующее"]
		self.assertEqual(self.flash.add_word("существующее", "existing"), "Такое слово уже есть в словаре")
	
	def test_English_first(self):
		self.assertEqual(self.flash.add_word("existing", "существующее"), "Первое слово должно быть русским")
	
	def test_Ok(self):
		self.words = []
		self.assertEqual(self.flash.add_word("существующее", "existing"), "Добавлено слово 'существующее'")

if __name__ == "__main__":
	unittest.main()