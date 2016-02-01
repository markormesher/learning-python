class Person:

	# fields
	hobbies = []

	# constructor method - creates an instance
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age

	# toString method
	def __str__(self):
		return self.firstname + ' ' + self.lastname + ' (' + str(self.age) + ')'

	# self-defined method
	def intro(self):
		print('Hi, I\'m ' + self.firstname + ' ' + self.lastname + ' and I am ' + str(self.age) + ' years old.')
		if len(self.hobbies) == 0:
			print('I have no hobbies')
		else:
			print('I have some hobbies: ' + str(self.hobbies))

	def addHobby(self, hobby):
		self.hobbies.append(hobby)
