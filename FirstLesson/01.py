teststr = input("Введите строку для проверки: ", )
if teststr[0] != 'a' or len(teststr) > 10 or teststr[-1] < 'a' or teststr[-1] > 'z':
    print('No')
else:
    print('Yes')