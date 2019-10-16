import math as m

for x in list(range(5, 11)):
    x *= 0.2
    print(x, m.cos(x) * m.exp(-x))
