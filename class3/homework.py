import math
from typing import Union

# 1 and 2

class Fracton:
	def __init__(self, a:int = 0, b:int = 0) -> None:
		self.a = a
		self.b = b

	def __eq__(self, other: Union[int, float, 'Fracton']) -> bool:
		if isinstance(other, int | float):
			return self.a / self.b == other
		else:
			return self.a / self.b == other.a / other.b
		
	def __ne__(self, other: Union[int, float, 'Fracton']) -> bool:
		if isinstance(other, int | float):
			return self.a / self.b != other
		else:
			return self.a / self.b != other.a / other.b
		
	def __gt__(self, other: Union[int, float, 'Fracton']) -> bool:
		if isinstance(other, int | float):
			return self.a / self.b > other
		else:
			return self.a / self.b > other.a / other.b

	def __lt__(self, other: Union[int, float, 'Fracton']) -> bool:
		if isinstance(other, int | float):
			return self.a / self.b < other
		else:
			return self.a / self.b < other.a / other.b

	def __ge__(self, other: Union[int, float, 'Fracton']) -> bool:
		if isinstance(other, int | float):
			return self.a / self.b >= other
		else:
			return self.a / self.b >= other.a / other.b

	def __le__(self, other: Union[int, float, 'Fracton']) -> bool:
		if isinstance(other, int | float):
			return self.a / self.b <= other
		else:
			return self.a / self.b <= other.a / other.b

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
			return Fracton(nums[0])
		elif len(nums) == 2:
			return Fracton(nums[0], nums[1])


	def __str__(self) -> str:
		if self.b == 0 and self.a == 0:
			return "0"
		if type(self.a) == str:
			return	self.__convert(self.a).__reduce()
		if self.b == 0 and self.a != 0:
			return f"{self.a}"
		return self.__reduce()
		

print(Fracton(-5, 10))
