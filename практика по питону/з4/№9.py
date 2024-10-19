# -- coding: utf-8 --

#Пользователь вводит число N с клавиатуры - количество чисел из ряда Фибоначчи. Посчитайте сумму этих чисел

def ph():
    n = int(input())
    if n == 1: return 0
    elif n == 2: return 1
    else:
        d1 = 0
        d2 = 1
        summa = 1
        for i in range(n-2):
            d_next = d1 + d2
            summa += d_next
            d1, d2 = d2, d_next
        return summa
print(ph())        
        
