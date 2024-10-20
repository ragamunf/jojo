# -- coding: utf-8 --

from math import *

x = 3.74*10**(-2)
y = -0.825
z = 0.16*10**2

ch = (1 + (sin(x+y))**2)*x**abs(y)
zn = abs(x - 2*y/(1+x**2*y**2))
s = ch/zn + (cos(atan(1/z)))**2
print('s = {0:.5f}'.format(s))

