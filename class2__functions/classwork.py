import time

def joiner(*words):
	return ' '.join(words)

def root(num, base = 2):
	return num**(1/base)



def remainder(num, div):
	return num % div

def tracer(func, *args, **kwargs):
	for arg in args:
		print(arg)
	
	for key in kwargs:
		print(f'{key} -> {kwargs[key]}')
	
	print(func(*args, **kwargs))



def timeSpended(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(end - start)
		return result
	return wrapper

@timeSpended
def wait(sec):
	time.sleep(sec)
	return f'after {sec} seconds'