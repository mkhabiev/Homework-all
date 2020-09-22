#monkey_trouble
monkey1 = bool(int(input('0 or 1: ')))
monkey2 = bool(int(input('0 or 1: ')))
if monkey1 and monkey2 or not monkey1 and not monkey2:
    print(True)
else:
    print(False)