#Python – Extract Unique values dictionary values
def extract_unique_values(dictionary):
    all_values = [value for values in dictionary.values() for value in values]
    unique_values = list(set(all_values))
    return unique_values

# Example usage:
my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}

result = extract_unique_values(my_dict)

print("Original Dictionary:", my_dict)
print("Unique Values:", result)
