#Python | Ways to remove a key from dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
else:
    print(f"The key '{key_to_remove}' is not present in the dictionary.")

print("Updated Dictionary:", my_dict)
