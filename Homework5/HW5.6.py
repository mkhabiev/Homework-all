#close_far
def close_far(a, b, c):
 return (abs(b - c)>=2) and (abs(b - a) <= 1) and (abs(c - a) >= 2) or (abs(c - a) <= 1) and (abs(b - a) >=2)