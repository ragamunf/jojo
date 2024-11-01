def main(a, b):
    a, b = b, a
    return a, b

from random import *

a = [randint(0,50) for i in range(10)]
b = [randint(0,50) for i in range(10)]
print(a, b, sep='\n')
print()
print('Меняем местами содержимое массивов:')
a, b = main(a, b)
print(a, b, sep='\n')
    
