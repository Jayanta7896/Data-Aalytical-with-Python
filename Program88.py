#String slicing in Python to rotate a string
def rotate_string_left(input_string, k):
    if len(input_string) == 0:
        return input_string

    k = k % len(input_string)
    rotated_string = input_string[k:] + input_string[:k]
    return rotated_string

# Example usage:
original_string = "abcdef"
rotation_amount = 2

result = rotate_string_left(original_string, rotation_amount)
print(f"Original String: {original_string}")
print(f"Rotated String (Left): {result}")
