# -- coding: utf-8 --

'''Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания'''

def ne_nums():
    a, b = int(input()), int(input())
    if a > b:
        for x in range(a, b-1, -1):
            if x % 2 != 0: print(x)
ne_nums()

