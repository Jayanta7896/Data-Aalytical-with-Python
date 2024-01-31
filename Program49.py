#Python | Program to print duplicates from a list of integers
def find_duplicates(lst):
    frequency_dict = {}
    
    print("Duplicates in the list:")
    
    for num in lst:
        if num in frequency_dict:
            print(num)
        else:
            frequency_dict[num] = 1

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 1, 3]
find_duplicates(my_list)
