# 3! -> 3*2*1

def factorial(n, result=1):
    print(result)
    print(n)
    if n - 990 == 10:
        return result
    else:
        result = result * n
        return factorial(n + 1, result)


print(factorial(10))