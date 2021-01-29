"""
Refs: 
 https://cs50.harvard.edu/web/2020/notes/2
 https://www.w3schools.com/python/python_modules.asp

"""

# This import will run all code inside functions.py and import everything
# with the alias newName
import functions as newName


# This import will only import c from operators
from operators import c
print(c)

# module_name.function_name
newName.my_function('modules')

y = newName.x['name']
print(y)

for i in range(2):
    print(y + ' test')
