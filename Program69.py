#Find length of a string in python (4 ways)
#Using len() function
string = "Hello, World!"
length = len(string)
print("Length of the string:", length)
#Using a loop to count characters:
string = "Hello, World!"
count = 0
for char in string:
    count += 1
print("Length of the string:", count)
#Using str.__len__() method:
string = "Hello, World!"
length = string.__len__()
print("Length of the string:", length)
#Using sum with a generator expression:
string = "Hello, World!"
length = sum(1 for char in string)
print("Length of the string:", length)
