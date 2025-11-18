try:
    with open("числа.txt", "r", encoding="utf-8") as fh:
        lines = fh.readlines()
except Exception as e:
    print("Ошибка при работе с файлом:", e)
    lines = []

if lines:
    numbers = []
    for i in lines:
        try:
            numbers.append(int(i))
        except ValueError:
            continue
    if numbers:
        with open("числа.txt", "a", encoding="utf-8") as fh:
            fh.write(str(sum(numbers)) + "\n")
            fh.write(str(max(numbers)))
