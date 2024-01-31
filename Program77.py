#Generating random strings until a given string is generated
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_until_target(target_string):
    generated_string = ""
    attempts = 0

    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
        attempts += 1

    return generated_string, attempts

# Example usage:
target_string = "Hello123"
result, num_attempts = generate_until_target(target_string)

print(f"Target String: {target_string}")
print(f"Generated String: {result}")
print(f"Number of Attempts: {num_attempts}")
