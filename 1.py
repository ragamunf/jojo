def f(numbers):
    for item in numbers:
        if not isinstance(item, int):
            return numbers
    return tuple(sorted(numbers))

t = (1, 8, 8, 2, 3)
print(f(t))