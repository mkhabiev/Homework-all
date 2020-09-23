#last2
word = input('Give a word: ')
count = 0
for i in range(len(word)-2):
    if word[i:i+2] == word[-2:]:
      count += 1
print(count)