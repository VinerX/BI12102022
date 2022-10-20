import random


def MakeMassive(Massive, Size):
    for i in range(Size): # Добавляю в массив рандомные числа
        number = random.randint(-1000, 1000)/10
        Massive.append(number)
    print(Massive)

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
    MakeMassive(A, SizeA) # С помощью функции я немного сократил повторяющийся код
    MakeMassive(B, SizeB)
    for i in A: # Поиск общего
        if i in B:
            Common.append(i)
    print("Общие: ", Common)