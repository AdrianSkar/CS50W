# multiple assignment
# Ref: https://cs50.harvard.edu/web/2020/notes/2

a, b = 1, True

print(a, b)


# Strings (ordered, immutable)
str = 'name'
print(str[0])

# Lists (ordered, mutable)
list = ['one', 'two', 'three']
list.append('four')
print(list)
print(list[3])
list.sort()
print(list)

# Tuples (ordered, immutable): generally for storing a couple of values
point = (10.2, 10.8)
print(point[1])

# Sets (unordered, mutable through methods), unique values
s = set()
test = (1, '2')
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(test)

print(s)
s.remove(2)
print(s)

# Dictionaries (unordered, immutable); key-value
dict = {'prop1': 1, 'prop2': 'two'}
print(dict)
dict['prop2'] = 'Two'
print(dict['prop2'])
print(len(dict))

