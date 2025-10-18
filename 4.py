from collections.abc import Hashable

t = [2, 2, 3, [9, 10], 'c']
t_for_set = []
for item in t:
    if isinstance(item, Hashable):
        t_for_set.append(item)
    else:
        continue

print(set(t_for_set))