#in1to10
x = int(input('x: '))
mode = input('True or False: ')
if 10 >= x >= 1:
    print(True)
elif (x <= 1 or x >= 10) and  mode == True:
    print(True)
else:
    print(False)