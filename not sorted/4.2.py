import math as m

def print_stairs():
  for i in range(N, 0, -1):
    for j in range(N, i - 1, -1):
      print(j, end =" ")
    print()

N = int(input("Enter N (from 1 to 9): "))

print("Variant 5: ")
print_stairs()
