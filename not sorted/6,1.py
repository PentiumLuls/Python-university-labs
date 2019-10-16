import math
import random

items = list(range(-10, 10))
random.shuffle(items)

print('List: ', str(items))

if(items == sorted(items)):
    print('Yes, list is sorted  ~~desu')
else:
    print('No, list isn`t sorted  ~~desu')
