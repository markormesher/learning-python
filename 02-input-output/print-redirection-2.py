# open a text file
outputFile = open('output-2.txt', 'a')

# write to it
print >> outputFile, 'hello'

# 'print()' still works
print('goodbye')
