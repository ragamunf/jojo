numbers = input().split()
numbers = [int(x) for x in numbers]

index = True
for x in numbers:
    if x <= 0:
        index = False
        break
print("Все элементы списка являются положительными числами:", index)
index = all([x > 0 for x in numbers])
print("Все элементы списка являются положительными числами:", index)

print("")
index = False
for x in numbers:
    if x == 0:
        index = True
        break
print("В списке есть хотя бы один нулевой элемент:", index)
index = any([x == 0 for x in numbers])
print("В списке есть хотя бы один нулевой элемент:", index)

print("")
index = False
for x in numbers:
    if x % 2 != 0:
        index = False
        break
print("Все элементы списка являются четными числами:", index)
index = all([x % 2 == 0 for x in numbers])
print("Все элементы списка являются четными числами:", index)

print("")
index = False
for x in numbers:
    if x % 2 != 0:
        index = True
        break
print("В списке есть хотя бы один нечетный элемент:", index)
index = any([x % 2 != 0 for x in numbers])
print("В списке есть хотя бы один нечетный элемент:", index)