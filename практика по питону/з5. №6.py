# -- coding: utf-8 --

count = 0
x = int(input())
s = x
while x != 0:
    x = int(input())
    count += 1
    s += x
print(s/count)
