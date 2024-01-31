#Find words which are greater than given length k
def find_words_greater_than_k(input_string, k):
    words = input_string.split()
    result_words = [word for word in words if len(word) > k]
    return result_words

# Example usage:
input_string = "This is a sample string with words of varying lengths"
k = 4
result = find_words_greater_than_k(input_string, k)

print(f"Original String: {input_string}")
print(f"Words greater than length {k}: {result}")
