import unittest
from app.flashcards import FlashCards

class Test_delete(unittest.TestCase):
	def setUp(self) -> None:
		self.flash = FlashCards()
	
	def test_TypeMismatch_1(self):
		self.assertEqual(self.flash.delete_word(123), "Неправильный тип ввода")
	
	def test_TypeMismatch_2(self):
		self.assertEqual(self.flash.delete_word(True), "Неправильный тип ввода")
	 
	def test_Empty_1(self):
		self.assertEqual(self.flash.delete_word(''), "Введите данные")

	def test_Empty_2(self):
		self.assertEqual(self.flash.delete_word('      '), "Введите данные")
	
	def test_Non_existing(self):
		self.flash.words = ["существующее"]
		self.flash.engs = ["existing"]
		self.assertEqual(self.flash.delete_word("несуществующее"), "Такого слова нет в словаре")
	
	def test_Allright(self):
		self.flash.words = ["существующее"]
		self.flash.engs = ["existing"]
		self.assertEqual(self.flash.delete_word("существующее"), "Удалено слово 'существующее'")

if __name__ == "__main__":
	unittest.main()