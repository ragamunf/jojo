p = float(input("Грузоподъемность грузовика: "))
items = []
count = 1

while True:
    i = input(f"{count}й предмет имеет массу: ")
    if i == "":
        break
    items.append(float(i))
    count += 1

total = 0
for item in items:
    total += item
    if total > p:
        print("Перевозка груза невозможна")
        break
else:
    print("Перевозка груза возможна")