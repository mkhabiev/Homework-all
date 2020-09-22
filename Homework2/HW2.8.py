#parrot_trouble
hour = int(input("Hour: "))
talking = input('True or False: ' )
if (0 <= hour <= 7 or 20<= hour <= 23) and talking :
    print(True)
else:
    print(False)