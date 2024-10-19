# -- coding: utf-8 --

#Определить, сколько раз в тексте встречается заданное слово

def meet(s, t):
    for i_word in range(len(t)):
        for symbol in t[i_word]:
            if not symbol.isalpha():
                t[i_word] = t[i_word].replace(symbol, '') 
    return t.count(s)
s = input('Введите заданное слово: ').lower()
t = input('Введите текст: ').lower().split()
print(meet(s, t))
