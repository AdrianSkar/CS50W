"""
Ref:
 https://cs50.harvard.edu/web/2020/notes/2


Higher order functions that can modify another functions
"""


def announce(f):
	def wrapper():
		print("About to run the function...")
		f()
		print("...done running the function.")
	return wrapper


@announce
def hello():
	print('Hello world')


hello()
