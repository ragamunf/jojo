# -- coding: utf-8 --

'''Дано число n. С начала суток прошло n минут. Определите,
сколько часов и минут будут показывать электронные часы в этот момент.
Программа должна вывести два числа: количество часов (от 0 до 23)
и количество минут (от 0 до 59). Следует предусмотреть случай, когда количество
введенных минут больше чем кол-во минут в сутках.'''

def time(n):
    thisd = n%(24*60)
    hs = thisd//60  
    mins = thisd%60
    if len(str(mins))==1:
        print(f'{hs}:0{mins}')
    else:
        print(f'{hs}:{mins}')

N = int(input())
time(N)


