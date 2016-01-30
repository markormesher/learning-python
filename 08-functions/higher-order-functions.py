# map - applies a function to a set of values
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# filter - returns only the criteria that meet a condition
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

# reduce - applied a binary function to the first two elements of a list, replacing them with the result, and recursing until one value remains
import functools
print(functools.reduce(lambda x, y: x + y, range(1, 11)))
