#String slicing in Python to check if a string can become empty by recursive deletion
def can_become_empty(input_string, target_string):
    if input_string == target_string:
        return True

    for i in range(len(input_string)):
        substring = input_string[:i] + input_string[i+1:]
        if can_become_empty(substring, target_string):
            return True

    return False

# Example usage:
input_str = "abc"
target_str = ""

result = can_become_empty(input_str, target_str)

if result:
    print(f"The string '{input_str}' can become empty by recursive deletion.")
else:
    print(f"The string '{input_str}' cannot become empty by recursive deletion.")
