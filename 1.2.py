try:
    with open("числа.txt", "r+", encoding="utf-8") as fh:
        numbers = fh.readlines()
        numbers = [float(i.strip("\n")) for i in numbers]
        fh.write(str(sum(numbers)) + "\n")
        fh.write(str(max(numbers)))
except Exception as e:
    print("Ошибка при работе с файлом:", e)
