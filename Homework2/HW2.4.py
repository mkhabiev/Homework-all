#sleep_in
day = input('Write name of the date ')
weekday = ('Monday, Tuesday, Wednesday Thursday, Friday')
vacation = ('Saturday, Sunday')

if day in weekday:
  print(True)
elif day not in weekday or vacation:
    print(False)
elif day in vacation:
  print(False)
else:
    print(False)