# basic example
def square(n):
	return n * n

sqNum = square
print(sqNum(5)) # 5

# map example
print(list(map(square, [1, 2, 3, 4, 5])))

# callback example
def callback(n):
	print('Callback called with ' + str(n))

def someLongRunningAction(c):
	# something that takes a long time...
	c(42)

someLongRunningAction(callback)
