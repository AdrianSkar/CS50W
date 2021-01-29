"""
Ref:
 https://cs50.harvard.edu/web/2020/notes/2
 https://www.w3schools.com/python/python_lambda.asp

Small and anonymous short versions of functions. Helpful when we don't want to 
write a whole separate function for a single small use (see sort example).

lambda arguments(any):expression(one)

"""


def square(param):
	return param * param


print(square(2))

# Is the same as (where `lambda input:output`)


def squareL(x): return x * x


print(squareL(4))


# sort() won't work with dicts

people = [
	{'name': 'Timmy', 'age': 234},
	{'name': 'Aaron', 'age': 24},
	{'name': 'Kyle', 'age': 17}
]
# people.sort()  # TypeErr `< not supported between instances of dict and dict`
people.sort(key=lambda x: x['name'])
"""
Instead of:

def f(person):
	return person["name"]

people.sort(key=f)
"""

print(people)


def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
