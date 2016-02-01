from person import Person

# Programmer extends Person
class Programmer(Person):

	# constructor
	def __init__(self, firstname, lastname, age, languages):
		# call the base constructor
		Person.__init__(self, firstname, lastname, age)

		# add extras to this class
		self.languages = languages

	def __str__(self):
		return self.firstname + ' ' + self.lastname + ' (' + str(self.age) + ') ' + str(self.languages)
