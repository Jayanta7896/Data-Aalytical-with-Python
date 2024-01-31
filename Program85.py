#Python | Permutation of a given string using inbuilt function
from itertools import permutations

def string_permutations(input_string):
    # Generate all permutations of the string
    permuted_strings = permutations(input_string)

    # Convert each permutation tuple to a string and store in a list
    result = [''.join(permutation) for permutation in permuted_strings]

    return result

# Example usage:
input_string = "abc"
result = string_permutations(input_string)

print(f"Original String: {input_string}")
print(f"Permutations: {result}")
