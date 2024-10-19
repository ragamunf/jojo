# -- coding: utf-8 --

s = input('Введите заданное слово: ').lower()
f = input('Введите текст: ').split()
for i_word in range(len(f)):
    for symbol in f[i_word]:
        if not symbol.isalpha():
           f[i_word] = f[i_word].replace(symbol, '') 
    f[i_word] = f[i_word].lower()
print(f.count(s))
