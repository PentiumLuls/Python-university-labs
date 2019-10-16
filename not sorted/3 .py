x = int(input("Enter x: "))
b = int(input("Enter b: "))

result = 0

if x<0 and not b==0:
    result = (-x)**2 + b
elif x>0 and b==0:
    result = (x / (x - 3)) + b
else:
    result = -x / 3

print(result)
