#Python program to find Cumulative sum of a list
def cumulative_sum(lst):
    result = []
    current_sum = 0
    
    for num in lst:
        current_sum += num
        result.append(current_sum)
    
    return result

# Example usage:
my_list = [1, 2, 3, 4, 5]

cumulative_sum_list = cumulative_sum(my_list)
print("Original list:", my_list)
print("Cumulative sum list:", cumulative_sum_list)
