import random
A = []
B = []
Common = []

SizeA = input("Введите целое число - размер первого массива: ")
SizeB = input("Введите целое число - размер второго массива: ")

try:
    SizeA=int(SizeA)
    SizeB=int(SizeB)
    Check=True
except ValueError:
    print("Ввод некорректен, введите целые числа при новом запуске программы")
    Check=False

if Check:
    for i in range(SizeA): # Добавляю в массив A рандомные числа
        b = random.randint(-1000, 1000)/10
        A.append(b)
    print(A)

    for i in range(SizeB): # Добавляю в массив B рандомные числа
        b = random.randint(-1000, 1000)/10
        B.append(b)
    print(B)

    for i in A: # Поиск общего
        if i in B:
            Common.append(i)
    print(Common)