#love6
a = int(input('Number: '))
b = int(input('Number: '))
sum = a+b
if a==6 or b==6 or sum==6 or abs(a-b)==6 or abs(b-a)==6 or abs(-a-(-b))==6 or abs(-b-(-a))==6 or abs(-a+(-b))==6\
        or abs(-b+(-a))==6 :
    print(True)
else:
    print(False)