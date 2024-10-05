# -- coding: utf-8 --

a, b = int(input()), int(input())
if a < b:
    for x in range(a, b+1):
        print(x)
else:
    for x in range(a, b-1, -1):
        print(x)
