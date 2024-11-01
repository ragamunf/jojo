# -- coding: utf-8 --

def l():
    n = int(input('Введите длину массива: '))
    s = [float(input(f'Введите элемент {x}: ')) for x in range(n)]
    s_1 = [abs(a) for a in s]
    return min(s_1), s[::-1]
mn, s = l()
print(f'Минимальный элемент: {mn}')
print(s)
