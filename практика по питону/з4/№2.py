# -- coding: utf-8 --

'''Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания в противном случае.'''

def nums():
    a, b = int(input()), int(input())
    if a < b:
        for x in range(a, b+1): print(x)
    else:
        for x in range(a, b-1, -1): print(x)
nums()
