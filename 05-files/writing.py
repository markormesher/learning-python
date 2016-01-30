print('File name:')
name = raw_input()
print('Message:')
msg = raw_input()

f = open(name, 'w') # w = write
f.write(msg)
f.close()

print('Done')
