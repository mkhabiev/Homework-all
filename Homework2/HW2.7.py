#makes10
a = int(input("a: "))
b = int(input("b: "))
if a == 10 or b == 10:
    print(True)
elif a == 10 and b != 10 or a != 10 and b == 10:
    print(True)
elif (a + b) == 10:
    print(True)
elif (a + b) != 10:
    print(False)
else:
    print(False)