# -- coding: utf-8 --

n = int(input())
f, s = 1, 0
for x in range(1, n+1):
    f *= x
    s += f
print(s)
