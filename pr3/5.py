a = input("введите слово: ")
b = input("введите букву: ")
if b not in a:
    print("буквы {} нет в строке {}".format(b, a))
else:
    print(a.index(b), a.rindex(b))
