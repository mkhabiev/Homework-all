#front3
word = input('Write the word: ')
if len(word) <= 3:
   print(word + word + word)
elif len(word) >= 3:
   print(word[0:3] + word[0:3] + word[0:3])
