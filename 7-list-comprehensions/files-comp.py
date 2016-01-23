# before
file = open('numbers.txt')
numbers = file.readlines()
print(numbers)

# after
numbers = [n.rstrip() for n in open('numbers.txt')]
print(numbers)
