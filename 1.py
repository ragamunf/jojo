info = {}

info["фио"] = "Мовсарова Медина Рамзановна"
info["дата_рождения"] = "05/01/2007"
info["место_рождения"] = "Воронеж"

print(info)

info["хобби"] = ["чтение", "плавание", "музыка"]
info["хобби"].append("программирование")

info["животные"] = ("кошка Моти", "кошка Нана", "кот Джейк")

info["ЕГЭ"] = {}
info["ЕГЭ"].update(Математика=90, Русский_язык=97, Информатика=70)
info["ЕГЭ"].update(Физика=0)
info['ЕГЭ'].pop('Физика')

info["вузы"] = {}
info["вузы"].update(ВГУИТ=184, ВГУ=248)

print("Данные:")
print(info)
exams = sorted(info["ЕГЭ"].keys())
print("Предметы:", exams)
uni = sorted(info["вузы"].keys())
print("Вузы:", uni)

print("\nОтветы на вопросы:")

name = info['фио'].split()[1]
starts_with_vowel = name[0] in "АОУЫЭЯЮЁИЕ"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = int(info["дата_рождения"][3:5])
born_in_winter_or_summer = month in [12, 1, 2, 6, 7, 8]
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["хобби"])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))

print("* после окончания школы сдавал {} экз.".format(len(info["ЕГЭ"].keys())))

sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

# Количество вузов, в которые Вы проходите по баллам
# Подсказка: определить, проходите Вы или нет, можно простым сравнением
# суммы баллов с проходным баллом вуза - ``True/False``.
# Для того, чтобы определить количество таких вузов, преобразуйте
# сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
vuz_count = sum([int(sum_mark >= x) for x in info["вузы"].values()])
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))