# -- coding: utf-8 --

#Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.

def nums(a, b, c):
    return min(a, b, c)
a, b, c = int(input('первое число: ')), int(input('второе число: ')),\
          int(input('третье число: '))
print(nums(a, b, c))
    
