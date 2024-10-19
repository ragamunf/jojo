# -- coding: utf-8 --

#По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов

def st():
    n = int(input())
    for y in range(n+1):
        for x in range(1, y+1):
            print(x, end='')
        print()
st()
