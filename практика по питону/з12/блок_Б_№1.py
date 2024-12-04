# -- coding: utf-8 --

def f():
    a = int(input())
    if a == 0: return 0
    return max(a, f())

print(f())
