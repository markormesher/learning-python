# empty tuple
emptytuple = ()
print 'emptytuple = ' + str(emptytuple) # ()

# numbers
numbers = (1, 2, 3, 4)
print 'numbers = ' + str(numbers) # (1, 2, 3, 4)

# indexing
print 'numbers[1] = ' + str(numbers[1]) # 1

# slicing
print 'numbers[1:3] = ' + str(numbers[1:3]) # (2, 3)

# joining
print 'numbers + numbers = ' + str(numbers + numbers) # (1, 2, 3, 4, 1, 2, 3, 4)

# replicating
print 'numbers * 4 = ' + str(numbers * 4) # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# notes
print 'Note: - tuples are immutable'
print '      - tuples can be used as dictionary keys'
print '      - other than that, they\'re a lot like lists'
