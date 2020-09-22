#pos_neg
a = int(input('a: '))
b = int(input('b: '))
if a < 0 and b<0:
    print(True)
elif ((a<0 and b>0) or (a>0 and b<0)):
    print(True)
else:
    print(False)