#combo_string
a = input('Anything: ')
b = input('Anything: ')
if len(a) > len(b):
    print(b + a + b)
else:
  print(a + b + a)