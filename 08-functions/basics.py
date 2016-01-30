def square(n):
	return n * n

def numVowels(string):
	string = string.lower()
	count = 0
	for i in range(len(string)):
		c = string[i]
		if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
			count += 1
	return count

def avg(a, b, c):
	return (a + b + c) / 3.0

def ultimatePredicate(input):
	return input == 42

print('The square of 6 is ' + str(square(6)))
print('The number of vowels in "Hello world" is ' + str(numVowels('Hello world')))
print('The average of 54, 26 and 32 is ' + str(avg(54, 26, 32)))
print('Is 41 the answer? ' + str(ultimatePredicate(41)))
print('Is 42 the answer? ' + str(ultimatePredicate(42)))
print('Is 43 the answer? ' + str(ultimatePredicate(43)))
