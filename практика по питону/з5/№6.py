# -- coding: utf-8 --

#Определите среднее значение всех элементов последовательности, завершающейся числом 0

def ver():
    count = 0
    x = int(input())
    s = x
    while x != 0:
        x = int(input())
        count += 1
        s += x
    return s/count
print(ver())
