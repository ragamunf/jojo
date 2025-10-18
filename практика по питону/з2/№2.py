# -- coding: utf-8 --

import math
x, y, z = -4.5, 0.000075, -84.5
u = math.pow(9+(x-y)**2, 1/3)
d = x**2 + y**2 + 2
r = math.pow(math.e, math.fabs(x-y))*math.tan(z)**3
s = u/d - r
print('s = {0:.5f}'.format(s))
