#Python – Convert key-values list to flat dictionary
# List of key-value pairs
key_values_list = [('a', 1), ('b', 2), ('c', 3)]

# Convert to a flat dictionary
flat_dict = {key: value for key, value in key_values_list}

print("Original List of Key-Value Pairs:", key_values_list)
print("Flat Dictionary:", flat_dict)
