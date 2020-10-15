def exceptions():
    raise ValueError

def main():
    a = 1/0
    try:
        a = 1 / 0
    except Exception:
        return 'Error in this function'



print(main())