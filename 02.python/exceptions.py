"""
Ref:
 https://cs50.harvard.edu/web/2020/notes/2
 https://www.w3schools.com/python/python_try_except.asp
"""
import sys

try:
	x = int(input("x: "))
	y = int(input("y: "))
except:
	print("Error: Invalid input")
	sys.exit(1)

try:
	result = x / y
except ZeroDivisionError:
	print('Error: cannot divide by 0')
	sys.exit(1)
finally:
	print('This will be executed regardless.')

print(f"{x} / {y} = {result}")


missingVar = 45
try:
	print(missingVar)
except TypeError:
	print("This was a TypeError")
except:
	print('Something else happened')
else:
	print('Nothing went wrong')


# Raise exception
z = 'string'

if not type(z) is int:
	raise TypeError(f'Only numbers allowed, z is {type(z)}')
