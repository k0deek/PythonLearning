print("Введите 3 числа: ")
numbers = [int(input()) for i in range(3)]
max3 = max(numbers)
min3 = min(numbers)
print("Максимально число: ", max3)
print("Минимальное число: ", min3)
for numb in numbers:
    if numb != max3 and numb != min3:
        print("Оставшееся число: ", numb)
