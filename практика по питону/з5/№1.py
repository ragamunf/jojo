# -- coding: utf-8 --

#По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

def kw():
    n = int(input())
    i = 1
    while i**2 <= n:
        print(i**2)
        i += 1
kw()
