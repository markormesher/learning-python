# recursive factorial function
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)

print('0! = ' + str(factorial(0)))
print('1! = ' + str(factorial(1)))
print('5! = ' + str(factorial(5)))
print('9! = ' + str(factorial(9)))

print('')

# recursive string explosion
def explode(word):
	if len(word) <= 1:
		return [word]
	else:
		return [word[0]] + explode(word[1:])

print('explode(\'Hello world\') = ' + str(explode('Hello world')))
