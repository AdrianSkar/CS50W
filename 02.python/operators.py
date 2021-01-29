# Ref: https://www.w3schools.com/python/python_operators.asp

# Arithmetic ones
x = 2
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
# Floor division (returns the largest possible int)
print(x // y)

# Logical
print(x > 0 and y > 0)
print(not (x > 0 and y > 0))
print(x > 0 or y > 12)

# Identity
a = {}
b = a
print(a is b)
print(a is not b)

print(x is y)
print(x is not y)

# Membership
c = [1, 2, 3, 4, 5]
print(4 in c)
print(6 not in c)
