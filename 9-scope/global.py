# this variable has a global scope, with regards to the rest of the program
number = 42

# it can be accessed here...
print(number)

# and here...
def check():
	print(number)
check()
