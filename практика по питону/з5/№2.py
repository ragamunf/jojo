# -- coding: utf-8 --

#Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

def dl():
    n = int(input())
    x = 2
    while True:
        if n % x == 0:
            return x
            break
        x += 1
print(dl())

