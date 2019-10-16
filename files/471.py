def main():
    print(" ~Consider running this script from the file dir or change the file path to full instead of relative")
    f = open("assets/random_numbers.txt", 'r')

    lines = f.readlines()
    sum = 0
    mult = 1
    second_power_sum = 0
    for num in lines:
        sum += int(num)
        mult *= int(num)
        second_power_sum += int(num)**2

    print("sum =", sum)
    print("mult =", mult)
    print("sum of second-powered =", second_power_sum)
    print("last element =", lines[len(lines) - 1])

main()