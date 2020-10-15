#lone_sum
def lone_sum(a, b, c):
    i = 0
    if a != b and a != c:
        i += a

    if b != a and b != c:
        i += b

    if c != a and c != b:
        i += c

    return i