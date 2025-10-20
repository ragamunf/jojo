n = int(input())
numbers = [float(input()) for _ in range(n)]

p_numbers = [x for x in numbers if x > 0]
n_numbers = []
for x in numbers:
    if x < 0:
        n_numbers.append(x)

print("исходный список: ", numbers)
print("список положительных чисел: ", p_numbers)
print("список отрицательных чисел: ", n_numbers)

sr_ar = sum(p_numbers)/len(p_numbers)
print("среднее арифметическое первого списка: ", "{:.2f}".format(sr_ar))

m = 1
for x in n_numbers:
    m *= x
sr_geom = pow(m, 1/len(n_numbers))
print("среднее геометрическое второго списка: ", "{:.2f}".format(sr_geom))

