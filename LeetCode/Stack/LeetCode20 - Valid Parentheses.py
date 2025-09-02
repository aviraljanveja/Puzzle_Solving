# LeetCode 20 : Valid Parentheses
# Problem Link : https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    brackets = {')':'(', '}':'{', ']':'['}  # Dictionary to store pairs of opening and closing brackets.
    stack = []  # Initiating an empty Stack, implemented via the Python list.

    for char in s:  # Iterate over the characters in the given string.
        if char in brackets:  # if the current character is a closing bracket (one of the keys in the dictionary defined above)
            if stack and stack[-1] == brackets[char]:  # Then check if the stack is non-empty and if the last character added to the stack was the corresponding opening bracket
                stack.pop()  # If yes, then it is a valid pair, so we pop it off the stack.
            else:
                return False  # If not, then either the order or type of brackets is incorrect and hence function returns False.
        else:
            stack.append(char)  # On the other hand, if the current character is an opening bracket, then simply add it on top of the stack.

    return len(stack) == 0  # If the stack is empty in the end, it means all the bracket-pairs were valid and popped off the stack, thus we return True, otherwise False.


# Test cases
s1 = "()[]{}"
print(isValid(s1))  # Output = True

s2 = "([])"
print(isValid(s2))  # Output = True

s3 = "([)]"
print(isValid(s3))  # Output = False
