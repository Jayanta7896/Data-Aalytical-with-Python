#Python program to accept the strings which contains all vowels
def contains_all_vowels(input_string):
    vowels = set("aeiou")
    input_set = set(input_string.lower())

    return vowels.issubset(input_set)

# Example usage:
user_input = input("Enter a string: ")

if contains_all_vowels(user_input):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
