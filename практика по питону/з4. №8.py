# -- coding: utf-8 --

n = int(input())
if n <= 9:
    for y in range(n+1):
        for x in range(1, y+1):
            print(x, end='')
        print()
