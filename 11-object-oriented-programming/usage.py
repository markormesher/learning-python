from person import Person
from programmer import Programmer

# Person

me = Person('Mark', 'Ormesher', 22)

print('me = ' + str(me))
print('')

me.intro()
print('')

me.addHobby('Programming')
me.addHobby('Cooking')
me.intro()
print('')

# Programmer

me = Programmer('Mark', 'Ormesher', 22, ['Java', 'Node.js', 'Python', '+ more'])

print('me = ' + str(me))
print('')
