n = int(input('количество чисел: '))
k = int(input('номер числа, с которого нужно начать: '))
ph = [0, 1]
d1, d2 = 0, 1
for i in range(k+n-3):
    d_next = d1 + d2
    ph.append(d_next)
    d1, d2 = d2, d_next
print(sum(ph[k-1:k+n-1]))

        
        
