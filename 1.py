def task1():
    def ceaser(text, shift):
        """Вернуть измененную строку 'text' со сдвигом 'shift'.
        Параметры:
        - text (str): строка;
        - shift (int): свдиг.
        Результат:
        - str: измененная строка.
        Исключения:
            - TypeError: неверный параметр
            - ValueError: введенная строка содержит латинские буквы
        """
        # Набор кириллических букв
        if type(text) != str:
            raise TypeError('text должен быть строкой')
        if type(shift) != int:
            raise TypeError('shift должен быть целым числом')
        letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        for letter in text:
            if letter.isalpha():
                if letter.lower() in letters:
                    n_index = (letters.index(letter.lower()) + shift) % len(letters)
                    if letter.islower():
                        text = text.replace(letter, letters[n_index], 1)
                    else:
                        text = text.replace(letter, letters[n_index].upper(), 1)
                else:
                    raise ValueError("Строка не должна содержать буквы не из кириллицы.")
        return text
    try:
        text = input("строка: ")
        shift = int(input("сдвиг: "))
        encoded = ceaser(text, shift)
        decoded = ceaser(encoded, -shift)
        print("Зашифрованная строка:", encoded)
        print("Расшифрованная строка:", decoded)
    except TypeError as err:
        print("Ошибка: ", err, ". Проверьте введенные данные.", sep="")
    except ValueError as err:
        print("Ошибка:", err)

def task2():
    def power(x, y=2):
        """Вернуть x^y.
        Параметры:
            - x, y (int).
        Результат:
            - int.
        Исключения:
            - RecursionError: введена слишком большая степень для рекурсии
            - ZeroDivisionError: попытка возвести ноль в отрицательную степень
        """
        if y == 0:
            return 1
        elif y < 0:
            return 1 / power(x, -y)
        else:
            return x * power(x, y - 1)
    try:
        x = int(input("Число, возводимое в степень: "))
        y = int(input("Степень: "))
        print(power(x, y))
    except RecursionError:
        print("Превышен лимит глубины рекурсии из-за слишком большого показателя степени.")
    except ZeroDivisionError:
        print("Ноль нельзя возводить в отрицательную степень.")
    except Exception as err:
        print("Ошибка:", err)

def task3():
    # Дан список ФИО. Найти наиболее часто встречаемое отчество.
    # Если отчества нет, человек не учитывается в подсчете.
    try:
        n = int(input("Введите кол-во человек: "))
        if n < 0:
            raise ValueError("Кол-во человек должно быть положительным числом")
        middle_names = {}
        for i in range(n):
            fio = input("Введите ФИО через пробел: ").split()
            if len(fio) == 2:
                continue
            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
        print("В расчете участвовало человек:", n)
    except ValueError as err:
        print("Ошибка: ", err, ". Проверьте введенные данные.", sep="")
    except Exception as err:
        print("Ошибка:", err)

def task4():
    # В программе хранится словарь вступительных экзаменов вида Предмет=Баллы.
    # Узнать, проходит ли абитуриент на специальность, если нужно сдать
    # все перечисленные экзамены с не меньшим количеством баллов.
    необходимые_экзамены = {
        "Информатика": 80,
        "Математика": 85,
        "Русский язык": 75
    }
    print("""
Для определения возможности поступления, необходима информация о Вас. 
Для ввода экзамена и баллов введите их через |: Химия | 40. 
Для завершения ввода нажмите Enter.""")

    сданные_экзамены = {}
    while True:
        try:
            ввод = input("").strip()
            if ввод == "":
                break
            ввод = [x.strip() for x in ввод.split("|")]
            экзамен, балл = ввод
            if экзамен == "" or балл == "":
                raise ValueError("Не соблюден формат")
            сданные_экзамены[экзамен] = int(балл)
            if int(балл) < 0:
                raise ValueError("Балл не может быть отрицательным.")
            elif int(балл) > 100:
                raise ValueError("Балл не может быть больше 100.")
        except ValueError as err:
            print("Ошибка: ", err, ". Проверьте введенные данные.", sep="")
        except Exception as err:
            print("Ошибка: ", err, ". Проверьте введенные данные.", sep="")
    print("Ваши экзамены:")

    try:
        for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
            print("{}) {} {}".format(i, экзамен, балл))
        ok = False
        for необходимый_экзамен, баллы in необходимые_экзамены.items():
            if сданные_экзамены[необходимый_экзамен] < баллы:
                break
        else:
            ok = True
        print("Вы можете к нам поступить!" if ok else "Увы...")
    except KeyError:
        print("Ошибка: Экзамен не найден в списке необходимых.")
    except Exception as err:
        print("Ошибка:", err)
task4()