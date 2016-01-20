print('What is the answer?')
ans = int(raw_input())

if ans < 42:
	print('Too low')
elif ans == 42:
	print('Bingo!')
else:
	print('Too high')
