def giveAnswer(ans):
	if ans != 42:
		raise Error()
	else:
		print('The answer is ' + str(ans))

try:
	giveAnswer(42)
	giveAnswer(43)
except:
	print('You gave the wrong answer!')
