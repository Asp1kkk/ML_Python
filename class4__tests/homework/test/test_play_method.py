import unittest
from app.flashcards import FlashCards

class Test_delete(unittest.TestCase):
	def setUp(self) -> None:
		self.flash = FlashCards()