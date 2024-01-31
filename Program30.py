#Python | Multiply all numbers in the list
#Using a loop:
my_list = [1, 2, 3, 4, 5]

product = 1
for num in my_list:
    product *= num

print(f"The product of all numbers in the list is: {product}")
#Using functools.reduce()
from functools import reduce

my_list = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, my_list)

print(f"The product of all numbers in the list is: {product}")
