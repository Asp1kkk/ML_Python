import time

# 1

def numbers_action(*args, operator="sum"):
	result = 0 if operator == "sum" else 1
	for i in args:
		result = result + i if operator == "sum" else result * i
	return result

# 2

def format_return(func):
	def wrapper(*args, **kwargs):
		return f'result of function {func.__name__} with args {args}, kwargs {kwargs} is {func(*args, **kwargs)}'
	return wrapper

# 3

def slow_down(func):
	def wrapper(*args, slow_down = 0, **kwargs): # вот тут возник вопрос - почему выдавало ошибку если опциональный аргумент slow_down засунуть после kwargs'ов
		time.sleep(slow_down)
		return func(*args, **kwargs)
	return wrapper