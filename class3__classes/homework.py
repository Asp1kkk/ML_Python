import math
from typing import Union
import pymorphy2

# 1 and 2

class Fraction:
	def __init__(self, a:int = 0, b:int = 0) -> None:
		self.a = a
		self.b = b

	def __eq__(self, other: Union[int, float, 'Fraction']) -> bool:
		if isinstance(other, int | float):
			return self.a / (self.b if self.b != 0 else 1) == other
		else:
			return self.a / (self.b if self.b != 0 else 1) == other.a / (other.b if other.b != 0 else 1)
		
	def __ne__(self, other: Union[int, float, 'Fraction']) -> bool:
		if isinstance(other, int | float):
			return self.a / (self.b if self.b != 0 else 1) != other
		else:
			return self.a / (self.b if self.b != 0 else 1) != other.a / (other.b if other.b != 0 else 1)
		
	def __gt__(self, other: Union[int, float, 'Fraction']) -> bool:
		if isinstance(other, int | float):
			return self.a / (self.b if self.b != 0 else 1) > other
		else:
			return self.a / (self.b if self.b != 0 else 1) > other.a / (other.b if other.b != 0 else 1)

	def __lt__(self, other: Union[int, float, 'Fraction']) -> bool:
		if isinstance(other, int | float):
			return self.a / (self.b if self.b != 0 else 1) < other
		else:
			return self.a / (self.b if self.b != 0 else 1) < other.a / (other.b if other.b != 0 else 1)

	def __ge__(self, other: Union[int, float, 'Fraction']) -> bool:
		if isinstance(other, int | float):
			return self.a / (self.b if self.b != 0 else 1) >= other
		else:
			return self.a / (self.b if self.b != 0 else 1) >= other.a / (other.b if other.b != 0 else 1)

	def __le__(self, other: Union[int, float, 'Fraction']) -> bool:
		if isinstance(other, int | float):
			return self.a / (self.b if self.b != 0 else 1) <= other
		else:
			return self.a / (self.b if self.b != 0 else 1) <= other.a / (other.b if other.b != 0 else 1)

	def __mul__(self, other) -> 'Fraction':
		if isinstance(other, Fraction):
			return Fraction(self.a * other.a, (self.b if self.b != 0 else 1) * (other.b if other.b != 0 else 1)).__reduce()
		
		if isinstance(other, int):
			return Fraction(self.a * other, self.b if self.b != 0 else 1).__reduce()
		
		if isinstance(other, float):
			return self.a / (self.b if self.b != 0 else 1) * other
	
	def __rmul__(self, other) -> 'Fraction':
		return self.__mul__(other)

	def __truediv__(self, other) -> 'Fraction':
		if isinstance(other, Fraction):
			return Fraction(self.a * (other.b if other.b != 0 else 1), (self.b if self.b != 0 else 1) * other.a).__reduce()
		
		if isinstance(other, int):
			return Fraction(self.a, (self.b if self.b != 0 else 1) * other).__reduce()

	def __rtruediv__(self, other) -> 'Fraction':
		return self.__truediv__(other)

	def __add__(self, other) -> 'Fraction':
		if isinstance(other, Fraction):
			lcm = math.lcm(self.b if self.b != 0 else 1, other.b if other.b != 0 else 1)
			mulForFirst = lcm/(self.b if self.b != 0 else 1)
			mulForSecond = lcm/(other.b if other.b != 0 else 1)
			return Fraction(int(self.a * mulForFirst + other.a * mulForSecond), lcm).__reduce()	
		if isinstance(other, int):
			return Fraction(self.a + other * (self.b if self.b != 0 else 1), (self.b if self.b != 0 else 1)).__reduce()

	def __radd__(self, other) -> 'Fraction':
		return self.__add__(other)

	def __iadd__(self, other) -> 'Fraction':
		return self.__add__(self.__add__(other))

	def __sub__(self, other) -> 'Fraction':
		if isinstance(other, Fraction):
			lcm = math.lcm(self.b if self.b != 0 else 1, other.b if other.b != 0 else 1)
			mulForFirst = lcm/(self.b if self.b != 0 else 1)
			mulForSecond = lcm/(other.b if other.b != 0 else 1)
			return Fraction(int(self.a * mulForFirst - other.a * mulForSecond), lcm).__reduce()	
		if isinstance(other, int):
			return Fraction(self.a - other * (self.b if self.b != 0 else 1), (self.b if self.b != 0 else 1)).__reduce()

	def __rsub__(self, other) -> 'Fraction':
		return self.__sub__(other)

	def __isub__(self, other) -> 'Fraction':
		return self.__sub__(self.__sub__(other))

	def __abs__(self) -> 'Fraction':
		return Fraction(abs(self.a), abs(self.b if self.b != 0 else 1)).__reduce()

	def __pos__(self) -> 'Fraction':
		return self.__abs__()

	def __neg__(self) -> 'Fraction':
		Fraction(-self.a, self.b if self.b != 0 else 1).__reduce()

	def __int__(self) -> int:
		return int(self.a / (self.b if self.b != 0 else 1))

	def __round__(self, nd) -> float:
		return round((self.a / (self.b if self.b != 0 else 1)), ndigits=nd)

	def __float__(self) -> float:
		return float(self.a / (self.b if self.b != 0 else 1))

	def __reduce(self):
		gcd = math.gcd(self.a, self.b)
		if self.b < 0:
			gcd = -gcd
		self.a //= gcd
		self.b //= gcd
		if self.b == 1:
			return f"{self.a}"
		return f"{self.a}/{self.b}"

	def __convert(self, string):
		if '/' in string:
			nums = [int(num) for num in string.split('/')]
		elif '-' in string:
			nums = [int(num) for num in string.split('-')]
		else:
			nums = [int(num) for num in string.split()]
		
		if len(nums) == 1:
			return Fraction(nums[0])
		elif len(nums) == 2:
			return Fraction(nums[0], nums[1])


	def __str__(self) -> str:
		if self.b == 0 and self.a == 0:
			return "0"
		if isinstance(self.a, str):
			return	self.__convert(self.a).__reduce()
		if self.b == 0 and self.a != 0:
			return f"{self.a}"
		return self.__reduce()
	
# 3
	
#class Sentence:
#	def __init__(self) -> None:
		
morph = pymorphy2.MorphAnalyzer()
print(morph)
#cats_parsed = morph.parse('котиков')[0]