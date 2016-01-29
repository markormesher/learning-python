def square(n):
	squared = n * n # 'square' is only in scope for the execution of this method
	return squared

print(square(2)) # 4
print(squared) # error
