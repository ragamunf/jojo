# -- coding: utf-8 --

x = float(input())  #км пробежал в 1 день
y = float(input())
count = 1  
while x < y:
    x += x/100*10
    count += 1
    #print(count, ":", x)
print(count)
