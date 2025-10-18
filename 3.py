def to_set(x):
    if isinstance(x, str):
        return set([int(item) for item in x.split()])
    return set(x)

t = [2, 2, 3]
set_t = to_set(t)
print("Полученное множество: {}, его мощность: {}".format(set_t, len(set_t)))