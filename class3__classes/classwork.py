class Circle:
	def __init__(self, radius, x, y):
		self.radius = radius
		self.x = x
		self.y = y
	
	def __del__(self): # вызовется когда произойдет удаление объекта garbage collector'ом
		print('Destroyed')

	def area(self):
		return self.radius**2 * 3.14
	
	def perimeter(self):
		return self.radius * 2 * 3.14

class Vector:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y
	
	def __add__(self, vector):
		return Vector(self.x + vector.x, self.y + vector.y)
	
	def __mul__(self, vector):
		return self.x * vector.x + self.y * vector.y
	
	def __neg__(self):
		return Vector(-self.x, -self.y)
	
	def __len__(self):
		return int((self.x**2 + self.y**2)**0.5)
	
	def __repr__(self) -> str:
		return f"coordinates: x: {self.x}, y: {self.y}"
	
#a = Vector(2, 3)
#b = Vector(3, 4)
#print(a)

#print(a + b)
#print(a * b)
#print(-a)
#print(len(a))
	
class User:
	name: str
	age: int
	__password: str

	def __init__(self, name, age, password) -> None:
		self.name = name
		self.age = age
		self._password = password

	def __private(self):
		return self.__password

class Vector3(Vector):
	def __init__(self, x, y, z) -> None:
		super().__init__(x = x, y = y)
		self.z = z
	
	def __repr__(self) -> str:
		return f"coordinates: x: {self.x}, y: {self.y}, z: {self.z}"
	
class LoggingDict(dict):
	def __init__(self, **kwargs) -> None:
		super().__init__(self, **kwargs)
		print("Created LoggingDict object")

	def __setitem__(self, key, value):
		super().__setitem__(key, value)
		print(f"Added key ")
	
class PositiveList(list):
	def __init__(self) -> None:
		super().__init__(self)
	
	def append(self, value) -> None:
		if value >= 0:
			super().append(value)
		else:
			raise Exception("The number must be positive")
	
pl = PositiveList()
pl.append(1)
print(pl)
pl.append(-1)