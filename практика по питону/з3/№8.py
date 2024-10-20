# -- coding: utf-8 --

'''Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны)'''

def nums(a, b, c):
    s = set([a, b, c])
    if len(s) == 1: return 3
    elif len(s) == 2: return 2
    elif len(s) == 3: return 0

a, b, c = int(input()), int(input()), int(input())
print(nums(a, b, c))
