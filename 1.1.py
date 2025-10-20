def f(x):
    if x >= 0:
        return x**0.5 + x**2
    else:
        return 1/x

print("{:.2f}".format(f(float(input()))))
