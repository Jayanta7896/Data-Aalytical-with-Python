#Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Displaying the original OrderedDict
print("Original OrderedDict:", ordered_dict)

# Inserting a new key-value pair at the beginning
ordered_dict.update({'x': 0})
ordered_dict.move_to_end('x', last=False)

# Displaying the updated OrderedDict
print("OrderedDict after insertion at the beginning:", ordered_dict)
