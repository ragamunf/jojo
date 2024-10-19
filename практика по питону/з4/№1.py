# -- coding: utf-8 --

'''Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.'''

a, b = int(input()), int(input())
def nums():
    for x in range(a , b+1): print(x)
nums()


