n = int(input())
l = [0]
while n:
    l.append(n)
    n = int(input())
print("Сумма введенных чисел:", sum(l))
print("Количество введенных чисел:", len(l))