s = "Известна масса каждого предмета в кг, загружаемого в грузовик."
letter = input()
s = s.split()

for word in s:
    if word.count(letter) != 0:
        s.remove(word)

print(" ".join(s))