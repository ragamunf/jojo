# -- coding: utf-8 --

def f(x):
    total = 1
    for i in x: total*= i
    print(f'для {x}\n произведение элементов равно: {total}, ср. ариф. равно: {sum(x)/len(x)}')

from random import *

a = [randint(12, 18) for x in range(4)]
b = [randint(0, 10) for x in range(6)]
c = [randint(19, 26) for x in range(5)]

f(a), f(b), f(c)


