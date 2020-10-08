#fashion_date
you = int(input('How stylish are you from 0 to 10: '))
date = int(input('How is your cloth from 0 to 10: '))
if you <= 2 or date <= 2:
    print(0)
elif you >= 8 or date >= 8:
    print(2)
else:
    print(1)