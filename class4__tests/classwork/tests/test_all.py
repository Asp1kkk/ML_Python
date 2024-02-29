import unittest
import datetime
from project.classwork import RuDateParser

class  ParserTests(unittest.TestCase):

	def setUp(self) -> None:
		self.parser = RuDateParser()

	def tearDown(self) -> None:
		pass

	def test_incorrectInput1(self):
		self.assertEqual(self.parser.parse_numeric("27 02 2024"), None)
	
	def test_incorrectInput2(self):
		self.assertEqual(self.parser.parse_numeric("not date"), None)
	
	def test_incorrectInput3(self):
		with self.assertRaises(TypeError) as context:
			self.parser.parse_numeric(37)
		
		self.assertTrue("No int in input" in str(context.exception))

	def test_day_too_large(self):
		self.assertEqual(self.parser.parse_numeric("90-09-2020"), None)
	
	def test_month_too_large(self):
		self.assertEqual(self.parser.parse_numeric("01-90-2020"), None)
	
	def test_day_zero(self):
		self.assertEqual(self.parser.parse_numeric("00-09-2020"), None)
	
	def test_month_zero(self):
		self.assertEqual(self.parser.parse_numeric("01-00-2020"), None)

	def test_first(self):
		self.assertEqual(self.parser.parse_numeric("01-01-1000"), datetime.datetime(day=1, month=1,year=1000))

if __name__ == "__main__":
	unittest.main()