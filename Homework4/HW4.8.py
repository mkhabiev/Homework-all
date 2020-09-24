#array_front9
found = False

for i in range(1, 10):
    num = int(input())

    if num == 9 and i < 5:
        found = True
        break


print(found)
