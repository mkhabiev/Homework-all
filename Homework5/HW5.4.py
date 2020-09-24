#no_teen_sum
def no_teen_sum(a, b, c):
    sum = a + b + c
    return sum


def fix_teen(n):
    if 13 <= n <= 19 and n != 15 and n != 16:
        return 0

    return n