import sys

# print() is actually doing this
sys.stdout.write('hello\n')

# re-write print to append to a file
sys.stdout = open('output-1.txt', 'a') # a = append

# now, print doesn't go to the console
print('This will be in the file')

# this changes 'print()' for the rest of the session though
# see print-redirection-2.py for a better option
