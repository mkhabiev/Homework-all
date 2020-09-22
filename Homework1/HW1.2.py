#caught_speeding
speed = int(input('Your speed: '))
birthday = input('True or False: ')
if (speed > 65 and 85 >= speed) and birthday == True:
   print(1)
elif speed >= 86 and birthday == True:
   print(2)
elif speed <= 65 and birthday == True:
   print(0)
elif 80 >= speed > 60:
   print(1)
elif speed >= 81 and birthday == True:
   print(1)
elif speed >= 81:
   print(2)
else:
   print(0)