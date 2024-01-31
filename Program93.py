#Python program to find the sum of all items in a dictionary
def sum_of_dict_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 30}

result = sum_of_dict_values(my_dict)

print("Original Dictionary:", my_dict)
print("Sum of Values:", result)
