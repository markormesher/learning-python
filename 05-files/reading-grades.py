f = open('grades.txt', 'r') # r = read
total = 0.0
count = 0
while True:
	grade = f.readline()
	if (grade == ''): break
	total += int(grade)
	count += 1

print('Count: %i' % count)
print('Total: %i' % total)
print('Average: %.3f' % (total/count))

