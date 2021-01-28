# Ref: https://www.w3schools.com/python/python_functions.asp

x = {
	"name": "Skar"
}


def my_function(param):
	print(f'Hello to {param} from a function')


my_function('you')
my_function('me')


# When multiple args are expected you can't provide less:

def anotherF(one, two):
	print(one + ' and ' + two)


anotherF('one', 'two')
# anotherF('one') # TypeError: missing arg


# `*args` will act somewhat like `arguments` would in JS

def arguments(*args):
	print('*args is: ', args)
	print('The 2nd item is: ', args[1])


arguments('first', 'second', 'third')

# `**args` will give the function a dictionary of arguments


def argDict(**args):
	print('**args is: ', args)
	print('The first name is: ', args['fname'])


argDict(fname='John', lname='Does')


# key = value syntax can be used with arguments

def keyvals(prop1, prop2):
	print('Props are: ', prop1, 'and', prop2)


keyvals(prop1='Property1', prop2='Property2')


# default params

def defParam(country="Norway"):
	print('I am from ' + country)


defParam('Spain')
defParam()
