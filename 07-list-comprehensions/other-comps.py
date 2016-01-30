n = range(1, 101)
even = [x for x in n if x % 2 == 0]
print(even)

msg = 'hello world this is dog'
words = msg.split(' ')
wordLengths = [(word, len(word)) for word in words]
print(wordLengths)
