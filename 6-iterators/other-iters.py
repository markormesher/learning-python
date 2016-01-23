import os

# range
numbers = range(1, 11)
rangeIt = iter(numbers)
print(next(rangeIt))

# file list
files = os.popen('ls ../')
filesIt = iter(files)
print(next(filesIt), end='')
print(next(filesIt), end='')
print(next(filesIt), end='')
print(next(filesIt), end='')
print(next(filesIt), end='')

# tuple
tup = (1, 2, 3, 4, 5)
tupIt = iter(tup)
print(next(tupIt))
print(next(tupIt))
print(next(tupIt))
