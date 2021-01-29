# Ref: https://docs.python.org/3/library/functions.html

import platform
c = [1, 2, 3, 4, 5]
d = ''

# all(iterable) Return True if any element of iterable is True


def all(param):
	for element in param:
		if element:
			return(True)
	return(False)


print(all(c))
print(all(d))

# bool(value) checks if Boolean
print(bool(True))
print(bool(''))

# dir returns the list of names in the current local scope, with arg attempts
# to return a list of valid attrs for that obj
print(dir())
print(dir(c))
print(c.__add__([11, 1, 2341]))
c.reverse()
print(c)


# evaluate an expression (expr must be a string)
d = 2
print(eval('d + 1'))


# filter (returns an iterator of filtered items)

def fun(a):
	if (a > 1):
		return True
	else:
		return False


e = filter(fun, c)
print(e)

for x in e:
	print(x)

#built-in platform
print(platform.system())
print(platform.version())
print(platform.processor())
print(platform.python_version())
print(platform.uname())
# Print all platform function names
print(dir(platform))
