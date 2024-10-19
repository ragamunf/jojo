# -- coding: utf-8 --

#По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.

def summa():
    n = int(input())
    s = 0
    for x in range(1, n+1): s += x**3
    print(s)
summa()
