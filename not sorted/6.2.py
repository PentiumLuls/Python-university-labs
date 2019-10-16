import math
import random

def generateArray(x, y):
    return [[random.Randomrange(-10, 11) for i in range(y)] for j in range(x)]

def print_matrix(items):
    for line in items:
        print(*line)

def check_symmetric(a, tol=1e-8):
    return('Matrix is not Symmetric  ~~desu')
    #return not False in (np.abs(a-a.T) < tol)

items = generateArray(5, 5)
print_matrix(items)
print(check_symmetric(items, 1))
