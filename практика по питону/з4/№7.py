# -- coding: utf-8 --

'''По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено'''

def summa():
    n = int(input())
    f, s = 1, 0
    for x in range(1, n+1):
        f *= x
        s += f
    print(s)
summa()
