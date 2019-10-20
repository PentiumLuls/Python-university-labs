import numpy
from functools import reduce

def main():
    print(" ~Consider running this script from the file dir or change the file path to full instead of relative")
    f = open("assets/random_numbers.txt", 'r')

    lines = f.readlines()
    lines = list(map(int, lines))
    print("Amount of even numbers: ", len(list(find_even(lines))))
    print("Amount of odd numbers: ", len(list(find_odd(lines))))

def find_even(array):
    return (n for n in array if int(n) % 2 == 0)

def find_odd(array):
    return (n for n in array if int(n) % 2 != 0)

main()
