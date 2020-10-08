#string_splosion
str = input('Word: ')
result = ''
for i in range(len(str)):
    result = result + str[:i + 1]
print(result)