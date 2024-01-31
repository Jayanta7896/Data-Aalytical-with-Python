#Python – Words Frequency in String Shorthands
def word_frequency(string):
    words = string.split()
    frequency = {word: words.count(word) for word in set(words)}
    return frequency

# Example usage:
input_string = "the quick brown fox jumps over the lazy dog the lazy dog barks loudly"
result = word_frequency(input_string)

# Print the word frequency
for word, count in result.items():
    print(f"{word}: {count} times")
