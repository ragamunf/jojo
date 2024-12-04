# -- coding: utf-8 --

def f(n):

    if n == 0: return 0
    return n%10 + f(n//10)

n = int(input('Введите число n: '))
print(f'Сумма цифр числа {n} равна: {f(n)}')
