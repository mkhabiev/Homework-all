#string_bits
word = input('Введите слово: ')
result = ''
for i in range(0, len(word)):
    if i%2 == 0:
      result += word[i]
print(result)