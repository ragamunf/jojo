# -- coding: utf-8 --

def matrix(file):
    # ввод матрицы
    a = []
    for row in file:
        a.append(list(map(float, row.split())))
           
    # поиск наибольшего элемента и его положения
    n = len(a)
    max_elem = a[0][0]
    row, column = 0, 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > max_elem:
                max_elem = a[i][j]
                row, column = i, j
                
    #удаление
    for i in range(n):
        a[i].pop(column)
    a.pop(row)
    
    return max_elem, a

with open('movsarovamr_u242_vvod.txt', 'r') as vvod, open('movsarovamr_u242_vivod.txt', 'w') as vivod:
    maximum, matx = matrix(vvod)
    for row in matx:
        vivod.write(' '.join(list(map(str, row)))+'\n')
    vivod.write(f'максимальный по модулю элемент: {maximum}')
