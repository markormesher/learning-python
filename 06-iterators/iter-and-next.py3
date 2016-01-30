numbers = [1, 2, 3, 4, 5]

# create an iteratror
it = iter(numbers)

# print them out
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# any more would cause a crash

# file = an iterator
fileIt = open('numbers.txt', 'r')
print(next(fileIt), end='')
print(next(fileIt), end='')
print(next(fileIt), end='')
print(next(fileIt), end='')
print(next(fileIt), end='')
