def max3(a,b,c = 5):
    if a <= b:
        if c <= b:
            return b
        else:
            return c
    elif a <= c:
        if b <= c:
            return c
        else:
            return b
    else:
        return a


print(max3(int(input()), int(input()), int(input())))