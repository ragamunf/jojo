# -- coding: utf-8 --

def matrix():
    k = int(input(f'Введите число k: '))
    n = int(input('Введите число строк: '))
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(int(input(f'Введите [{i}, {j}] элемент: ')))
        a.append(b)
    d = []
    for row in a:
        for elem in row:
            if elem % k == 0: d.append(elem)
    return d

res = matrix()
print(f'Количество искомых элементов: {len(res)}')
print(f'Максимальный из них: {max(res)}')
            

                 
                 
                 
