# -- coding: utf-8 --

n = int(input())
x = 2
while True:
    if n % x == 0:
        print(x)
        break
    x += 1
