# -- coding: utf-8 --

#Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

def var():
    x = int(input())
    y = 0
    cs = []
    count = 0
    while x != 0:
        if x == y: count += 1
        else: count = 1
        cs.append(count)
        y = x
        x = int(input())
    return max(cs)
print(var())
