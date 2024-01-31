#Reverse words in a given String in Python
def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string

# Example usage:
input_string = input("Enter a string: ")
result = reverse_words(input_string)

print("Original String:", input_string)
print("Reversed Words:", result)
