#Execute a String of Code in Python
code_to_execute = """
def say_hello():
    print("Hello, World!")

say_hello()
"""

try:
    exec(code_to_execute)
except Exception as e:
    print(f"Error executing code: {e}")
