#Find the longest word in a given string of words.
input = 'Hi this is just a test sentence used to find if the code is working or not 1234567'
stringsplit = input.split(' ')
ln = 0
words = ''
for word in stringsplit:
    if len(word) > ln:
        words = word
        ln = len(word)
w = [word for word in stringsplit if len(word) == ln]
print(w)

