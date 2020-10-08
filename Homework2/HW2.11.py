#missing_char
word = input('Write the word: ')
n = int(input("Number: "))
word = list(word)
word[n] = ''
print(''.join(word))