# -- coding: utf-8 --

'''Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.'''


def nums():
    a, b = int(input()), int(input())
    for x in range(a , b+1): print(x)
nums()


