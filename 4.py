l = []
while True:
    n = int(input())
    l.append(n)
    if n == 0:
        break
print("Сумма введенных чисел:", sum(l))
print("Количество введенных чисел:", len(l))