total = 0.0
count = 0
while True:
	print('Enter a number (-1 to quit):')
	try:
		grade = int(raw_input())
		if (grade == -1): break
		total += grade
		count += 1
	except ValueError:
		continue

print('Count: %i' % count)
print('Total: %i' % total)
print('Average: %.3f' % (total/count))
