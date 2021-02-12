from django.test import TestCase
from functools import reduce

# Create your tests here.


all = ['CSS', 'CSS3', 'Python']
query = 'c'

result = list(filter(lambda k: query in k, all))
print(result)

if result:
    print('yes')
else:
    print('no')


# strs = ['css', 'css3', 'python']

# def partial_result(query):
# 	output_list = []
# 	for test in query:
# 		if 'css' in test:
# 			output_list.append(test)
# 			print(f"{test}: yes")
# 		else:
# 			print(f"{test}: no")

# 	print(output_list)


# partial_result(strs)


# str = 'abc'
# print(str.find('bc'))


# test_entries = ['css', 'css3', 'python']

# query = 'css'
# for entry in test_entries:
# 	if entry.find(query) > -1:
# 		print(entry)
# 	else:
# 		print(f'not found in {entry}')

# output_list = ['asd']

# if output_list:
# 	print('yes')
# else:
# 	print('no')
