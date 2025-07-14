# A function is a block of organized, reusable code that performs a specific task.
# Functions promote code reusability, allowing the same block of code to be executed multiple times with different inputs.
# Functions help in organizing code into logical, manageable units, improving readability and maintainability.
# Python includes built-in functions like print() and len() and allows for user-defined functions.
# Lambda functions are another possibility that provide a concise way to create anonymous functions.


# Function definition
# Functions are defined using the def keyword, followed by the function name
# Parameters are listed within the parentheses of the function definition.
# Parameters are the variables listed in the function definition,
# acting as placeholders for the values that will be passed in, for example "n" here.
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
        # Functions can optionally return a value using the return statement.
        # If no return statement is present, the function implicitly returns None.

# Calling a function
# Arguments are the actual values that are passed to the function when it is called, for example 3 and 4 here.
print(isEven(3))  # Output = False
print(isEven(4))  # Output = True
