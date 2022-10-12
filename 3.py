import random

A = []
count=0

SizeA = input("Введите целое число - размер первого массива: ")
Delta = input("Введите целое число - значение Delta: ")

try:
    SizeA=int(SizeA)
    Delta=int(Delta)
    Check=True
except ValueError:
    print("Ввод некорректен, введите целые числа при новом запуске программы")
    Check=False


if Check:
    for i in range(SizeA): # Добавляю в массив A рандомные числа
        b = random.randint(-10, 10)
        A.append(b)
    print(A)

    MinNumber=min(A)
    for i in A:
        if i-Delta==MinNumber:
            count+=1
    print(f"Минимальное число {MinNumber}. От него на {Delta} отличаются {count} элементов")
