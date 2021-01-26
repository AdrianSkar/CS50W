## Ask for name and print it
# answer = input('Question: ')
# print("Hello, " + answer)
# print("Hello,", answer)  # auto space
# print(f"Hello, {answer}")

## Conditionals and loops
# x, y = 2, 20
# if x < y:
# 	print(f'{x} is less than {y}')
# elif x > y:
# 	print(f'{x} is more than {y}')
# else:
# 	print('They are equal')

# i = 3
# while i > 0:
# 	print(f'i in `while` is: {i}')
# 	i -= 1

# for i in [0, 1, 2]:  # same as `for i in range(3)`
# 	print('for')

## Scope across indentation but not across functions
# def main():
# 	i = get_positive_int()
# 	print(i)
# def get_positive_int():
# 	while True:
# 		n = int(input('Insert num: '))
# 		if n > 0:
# 			break
# 	print(f'{n} passes the test')
# 	return n  # Access to `n` is granted
# main()

## Iterate over string chars
# s = input('Insert string: ')
# print("Output: ", end='')  # end is set to empty string instead of default \n
# for c in s:
# 	# sep wont' work here because you are printing individual chars
# 	print(c, sep='A', end='')
# print()  # print \n

# print('a', 'b', sep='YAY')  # \n

# Swap values
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)


msg = 'asdf string'
print(msg)

# %%
msg = "Hello World"
print(msg)

# %%
msg = "Hello again"
print(msg)
