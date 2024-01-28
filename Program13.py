#Program to print ASCII Value of a character?
# Get input from the user
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    # Find and print the ASCII value
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is: {ascii_value}")
else:
    print("Please enter a single character.")
