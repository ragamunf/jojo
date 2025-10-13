a = []
b = []

a.append(4.5)
a.append(3.4)
a.extend([8.7, 1.3])

b.append(14.5)
b.append(3.4)
b.extend([8.7, 11.3])

a.insert(1, 100)
a.insert(3, 100)

b.insert(0, 200)
b.insert(2, 200)

print("Исходные списки:")
print("1-й:", a)
print("2-й:", b)

del a[0]
del b[0]

a.remove(100)
b.remove(200)

print("\nПосле удаления")
print("1-й:", a)
print("2-й:", b)

sa = set(a)
sb = set(b)
sa_and_sb = sa.intersection(sb)

print("\nУникальные элементы:")
print("1-й:", sa)
print("2-й:", sb)
print("общие:", sa_and_sb)

c = a + b

c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

sr_ar = 0
count_1 = 0
sr_geom = 1
count_2 = 0
for i, item in enumerate(c, start=1):
    if i % 2 == 0:
        sr_ar += item
        count_1 += 1
    else:
        sr_geom *= item
        count_2 += 1
sr_ar /= count_1
sr_geom **= 1/count_2

c_max = max(c)
c_min = min(c)

print("\nИтоговые:")
print("3-й:", c)
print("Сортировка (возр.):", c_asc)
print("Сортировка (убыв.):", c_desc)
print("Ср. арифм. =", sr_ar, "ср. геометр. =", round(sr_geom, 2))
print("Макс. и мин.:", c_max, c_min)


