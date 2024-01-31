#Python – Convert Snake case to Pascal case
def snake_to_pascal(snake_case):
    words = snake_case.split('_')
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

# Example usage:
snake_case_string = "hello_world_example"
pascal_case_result = snake_to_pascal(snake_case_string)
print("Snake Case:", snake_case_string)
print("Pascal Case:", pascal_case_result)
