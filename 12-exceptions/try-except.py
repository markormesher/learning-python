try:
	# code that may fail goes here
	thisWillFail = 12/0

except:
	# error handling code goes here
	print('Something went wrong!')

# alternative:

# except ZeroDivisionError:
#	error-specific handling code goes here
