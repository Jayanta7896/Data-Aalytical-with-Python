#Ways to sort list of dictionaries by values in Python – Using lambda function
# Sample list of dictionaries
list_of_dicts = [
    {'name': 'John', 'age': 25, 'score': 90},
    {'name': 'Alice', 'age': 22, 'score': 95},
    {'name': 'Bob', 'age': 28, 'score': 88}
]

# Sort the list of dictionaries by the 'score' key using a lambda function
sorted_list = sorted(list_of_dicts, key=lambda x: x['score'])

# Print the sorted list
print("Sorted List by Score:")
for item in sorted_list:
    print(item)
