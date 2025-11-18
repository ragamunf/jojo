numbers = input("Введите числа через пробел: ").split()

fh = None
try:
    fh = open("числа.txt", "w", encoding="utf-8")
    for i in numbers:
        fh.write(i + "\n")
finally:
    if fh:
        fh.close()