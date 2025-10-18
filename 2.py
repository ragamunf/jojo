def f(numbers, item):
    if item not in numbers:
        return ()

    first_occurrence = numbers.index(item)
    try:
        second_occurrence = numbers.index(item, first_occurrence + 1)
    except ValueError:
        return numbers[first_occurrence:]

    return numbers[first_occurrence:second_occurrence+1]
    
t = (1, 4, 5.6, "t", 8, 9, "t")
item = 9
print(f(t, item))
