#Python – Replace multiple words with K
import re

def replace_multiple_words(input_string, words_to_replace):
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, words_to_replace)) + r')\b', re.IGNORECASE)
    result = pattern.sub('K', input_string)
    return result

# Example usage:
input_string = "This is a sample sentence with multiple words. Words like apple, banana, and cherry need to be replaced."
words_to_replace = ["apple", "banana", "cherry"]

result = replace_multiple_words(input_string, words_to_replace)

print("Original String:", input_string)
print("String after replacing words:", result)
