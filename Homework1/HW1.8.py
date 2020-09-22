#alarm_clock
weekdays = [1, 2, 3, 4, 5]
weekends = [0, 6]
day = int(input('Day number: '))
vacation = input('True or False: ')

if (day == 0 or day == 6) and vacation == False:
    print('10:00')
elif (day >= 1 and day <= 5) and vacation == False:
    print('7:00')
elif (day == 0 or day == 6) and vacation == True:
    print('Off')
elif (day >= 1 and day <= 5) and vacation == True:
    print('10:00')