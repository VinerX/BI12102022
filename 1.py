import random

a = []
MaxNumber = -101
NumberPosition = 0


Size = input("Введите целое число - размер массива: ")
try:
    Size = int(Size)
    Check=True
except ValueError:
    print("Ввод некорректен, введите целое число при новом запуске программы")
    Check=False

if Check:
    for i in range(Size): # Добавляю в массив рандомные числа
        b = random.randint(-100, 100)
        a.append(b)
    print(a)

    for i in range(len(a)): #Ищю максимум и его номер
        if a[i] >= MaxNumber:
            MaxNumber = a[i]
            NumberPosition = i

    for i in range(len(a)): #Зануляю числа после максимума
        if i > NumberPosition:
            a[i] = 0

    print(a)



