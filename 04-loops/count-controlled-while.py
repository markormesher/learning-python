print('Numbers 1 to 20:')
number = 1
while number <= 20:
	print(number)
	number += 1

print('')

print('Sum of numbers 1 to 20:')
number = 1
sum = 0
while number <= 20:
	print(str(sum) + ' + ' + str(number) + ' = ' + str(number + sum))
	sum = number + sum
	number += 1

print('')

print('2.3% on 100 over 10 years:')
balance = 100
rate = 1.023
year = 1
while year <= 10:
	balance *= rate
	print('Balance after year ' + str(year) + ': ' + ('%.3f' % balance))
	year += 1
