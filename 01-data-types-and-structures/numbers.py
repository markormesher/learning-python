import math
import random

# integer will convert up to float
result = 1 + 3.14
print "1 + 3.14 is " + str(result) # 4.14

# order of operations
result = 1 + 2 * 3
print "1 + 2 * 3 is " + str(result) # 7

# order of operations
result = (1 + 2) * 3
print "(1 + 2) * 3 is " + str(result) # 9

# exponential
result = 10 ** 3
print "10 ** 3 is " + str(result) # 1000

# modulo
result = 346 % 37
print "346 % 37 is " + str(result) # 13

# exponential
result = math.pow(10, 3)
print "math.pow(10, 3) is " + str(result) # 1000.0

# square root
result = math.sqrt(144)
print "math.sqrt(144) is " + str(result) # 12.0

# floor
result = math.floor(3.999)
print "math.floor(3.999) is " + str(result) # 3.0

# ceiling
result = math.ceil(3.0001)
print "math.ceil(3.0001) is " + str(result) # 4.0

# random
result = random.random()
print "random.random() is " + str(result)

# random
result = random.randint(1, 50)
print "random.randint(1, 50) is " + str(result)
