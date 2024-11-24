# -- coding: utf-8 --

def matrix(file):
    mx = []
    for row in file:
        mx.append(list(map(int, row.split())))
    
    k = int(input('Введите число k: '))
    d = []
    for row in mx:
        for elem in row:
            if elem % k == 0: d.append(elem)
    return mx, d

with open('movsarovamedinaramzanovna_u242_vvod.txt', 'r') as vvod, \
     open('movsarovamedinaramzanovna_u242_vivod.txt', 'w') as vivod:
    mx, res = matrix(vvod)
    for row in mx:
        vivod.write(' '.join(list(map(str, row)))+'\n')
    vivod.write(f'Количество искомых элементов: {len(res)}, максимальный из них: {max(res)}')
