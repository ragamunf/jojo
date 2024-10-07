# -- coding: utf-8 --

n = int(input())
if n == 1: print(0)
elif n == 2: print(1)
else:
    d1 = 0
    d2 = 1
    s = 1
    for i in range(n-2):
        d_next = d1 + d2
        s += d_next
        d1, d2 = d2, d_next
    print(s)
        
        
