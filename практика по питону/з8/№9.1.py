# -- coding: utf-8 --

def f(n):
    global count
    if n!=0:
        n -= sum([int(x) for x in str(n)])
        count.append(n)
        f(n)
    return len(count)
       
n = int(input('введите число: '))
count = []
print(f(n))
        
