# -- coding: utf-8 --

def matrix():
    n = int(input('Введите порядок матрицы: '))
    
    # ввод матрицы
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(float(input(f'Введите [{i}, {j}] элемент: ')))
        a.append(b)
        
    print('исходная матрица:')
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()
        
    # поиск наибольшего элемента и его положения
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

maximum, matx = matrix()

print(f'максимальный по модулю элемент: {maximum}')
print('измененная матрица:')
for row in matx:
    for elem in row:
        print(elem, end=' ')
    print()          

                 
                 
                 
