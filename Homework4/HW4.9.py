#string_match
a = input('Word1: ')
b = input('Word2: ')

min_length = min(len(a), len(b))

count = 0
for i in range(min_length - 1):
    if a[i:i + 2] == b[i:i + 2]:
        count += 1
print(count)