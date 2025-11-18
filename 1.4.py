v_counter = 0
c_counter = 0

try:
    with open("стихотворение.txt", "r", encoding="utf-8") as fh:
        content = fh.read()
        print(content)
        content = content.split()
        for i in content:
            if i[0].lower() in "аеёиоуыэюя":
                v_counter += 1
            elif i[0].lower() in "бвгджзйклмнпрстфхцчшщ":
                c_counter += 1

except Exception as e:
    print("Ошибка:", e)
print()
if v_counter > c_counter:
    print("Больше слов, начинающихся на гласную")
elif v_counter < c_counter:
    print("Больше слов, начинающихся на согласную")
else:
    print("Количество слов, начинающихся на гласную и согласную, совпадает")
