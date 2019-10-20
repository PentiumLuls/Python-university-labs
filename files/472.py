import numpy
from functools import reduce

def main():
    print(" ~Consider running this script from the file dir or change the file path to full instead of relative")
    f = open("assets/random_numbers.txt", 'r')

    lines = f.readlines()
    lines = list(map(int, lines))
    print("Max element: ", find_max_iterable(iter(lines)))
    print("Min even element: ", find_min_iterable(find_even(lines)))
    print("Max odd element: ", find_max_iterable(find_odd(lines)))

def find_max_iterable(array):
    max = next(array, None)
    if max is not None:
       return reduce(lambda n,m: n if n > m else m, array, max)

def find_min_iterable(array):
    min = next(array, None)
    if min is not None:
        return reduce(lambda n,m: n if n < m else m, array, min)

def find_even(array):
    return (n for n in array if int(n) % 2 == 0)

def find_odd(array):
    return (n for n in array if int(n) % 2 != 0)

main()
