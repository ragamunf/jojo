a = ["машина", "яма", "якорь", "дети", "расположение", "он"]
l = max([len(x) for x in a])
new_a = []
for x in a:
    if len(x) < l:
        diff = l - len(x)
        new_x = x + "_"*diff
        new_a.append(new_x)
    else: new_a.append(x)
print(new_a)

