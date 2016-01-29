import math

def hypotenuse(s1, s2):
	# putting nested functions here is ridiculous, but it demonstrates the concept of nested scope
	def squareOfS1():
		return s1 * s1

	def squareOfS2():
		return s2 * s2

	return math.sqrt(squareOfS1() + squareOfS2())

print(hypotenuse(3, 4)) # 5.0
