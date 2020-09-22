#front_back
word = input('Write the word: ')
if len(word) <= 1:
    print(word)
print(word[-1] + word[1:-1] + word[0])
