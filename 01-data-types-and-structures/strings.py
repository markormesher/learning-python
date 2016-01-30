# concat
helloworld = 'Hello ' + 'World!'
print 'helloworld = ' + helloworld

# length
print 'len(helloworld) = ' + str(len(helloworld)) # 12

# indexing
print 'helloworld[0] = ' + str(helloworld[0]) # 'H'

# slicing
print 'helloworld[0:4] = ' + str(helloworld[0:4]) # 'Hell'
print 'helloworld[:6] = ' + str(helloworld[:6]) # 'Hello '
print 'helloworld[3:] = ' + str(helloworld[3:]) # 'lo World!'

# repeating
print 'helloworld*3 = ' + helloworld*3 # 'Hello World!Hello World!Hello World!'

# splitting
print 'helloworld.split(\' \') = ' + str(helloworld.split(' ')) # ['Hello', 'World!']
