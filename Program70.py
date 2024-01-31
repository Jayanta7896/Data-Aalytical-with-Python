#Python program to print even length words in a string
def print_even_length_words(input_string):
    words = input_string.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    
    print("Even length words in the string:")
    for word in even_length_words:
        print(word)

# Example usage:
input_string = "Python is a programming language with elegant syntax"
print_even_length_words(input_string)
