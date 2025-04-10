# -- coding: utf-8 --

from math import *
x, y, z = 14.26, -1.22, 0.035
u = 2*cos(x - 2/3)*(1 + (pow(z, 2)/(3 - pow(z, 2)/5)))
d = 1/2 + pow(sin(y), 2)
s = u/d
print('s = {0:.6f}'.format(s))
