#lucky_sum
def lucky_sum(a, b, c):
  sum = a + b + c
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  else:
    return a + b + c