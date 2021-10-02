ticket = [int(i) for i in input()]
if ticket[0]+ticket[1]+ticket[2] == ticket[3]+ticket[4]+ticket[5]:
    print("Счастливый")
else:
    print("Обычный")
