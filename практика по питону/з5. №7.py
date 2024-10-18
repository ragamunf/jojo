# -- coding: utf-8 --

count = -1
x = int(input())
y = 0
while x != 0:
    if x > y:
        count += 1
    y = x
    x = int(input())
print(count)
