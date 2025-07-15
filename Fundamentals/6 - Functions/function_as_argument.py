# Functions as arguments to other functions.

# In Python, functions are treated as first-class objects,
# meaning they can be assigned to variables, stored in data structures,
# and passed as arguments to other functions, just like any other data type (integers, strings, etc.)

# Demonstrating how functions can be passed as arguments to other functions.
# We have three functions: greet, name and display_message.
def greet():
    return "Hello "


def name():
    return "Alice!"


def display_message(greeting_function, name_function):
    # The display_message function takes two function parameters, message_function and name_function.
    # Note, we do not apply parentheses when using functions as parameters/arguments.
    message = greeting_function() + name_function()
    print(message)


# Pass 'greet' and 'name' functions as arguments to the 'display_message' function
display_message(greet, name)  # Output = Hello Alice!
