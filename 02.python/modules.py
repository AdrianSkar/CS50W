# This import will run all code inside functions.py and import everything
import functions as newName
import platform

# This import will only import c from operators
from operators import c
print(c)

# module_name.function_name
newName.my_function('modules')

y = newName.x['name']
print(y)

#built-in platform
print(platform.system())
print(platform.version())
print(platform.processor())
print(platform.python_version())
print(platform.uname())
# Print all platform function names
print(dir(platform))
