try:
	fail = 12/0
except:
	print('Something went wrong!')
finally:
	print('This will always run!')
