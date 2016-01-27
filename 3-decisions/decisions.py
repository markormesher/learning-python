print('What is the answer?')
ans = int(raw_input())

# if
if ans < 42:
	print('Too low')
# else if
elif ans == 42:
	print('Bingo!')
# else
else:
	print('Too high')
