f = open('grades.txt', 'w')
while True:
	print('Enter grade (q to quit):')
	grade = raw_input()
	if (grade == 'q'): break
	f.write(grade + '\n')
f.close()
