import unittest
from app.flashcards import FlashCards

class Test_delete(unittest.TestCase):
	def setUp(self) -> None:
		self.flash = FlashCards()
	
	def test_Empty(self):
		self.flash.words = []
		self.assertEqual(self.flash.play(), "В словаре нет слов")

if __name__ == "__main__":
	unittest.main()