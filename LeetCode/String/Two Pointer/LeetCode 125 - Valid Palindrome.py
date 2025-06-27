# LeetCode 125 - Valid Palindrome
# Problem Link : https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    s1 = ""  # Initialize an empty string to store the cleaned version of the input
    for char in s:  # Iterate through each character
        if char.isalnum():  # If the character is alphanumeric, add it to the cleaned string
            s1 += char.lower()

    return s1 == s1[::-1]  # Check if the cleaned string is equal to its reverse (palindrome check)

    # Second option : Two-pointer technique to check for a palindrome.
    # i = 0  # Pointer 1 : Start of string
    # j = len(s1) - 1  # Pointer 2 : End of String
    # while i < j:  # Use a while loop to compare characters from both ends moving towards the center
    #     if s1[i] != s1[j]:  # If the characters at the current pointers do not match, return False (not a palindrome)
    #         return False
    #     i += 1  # Move the left pointer to the right
    #     j -= 1  # and the right pointer to the left
    # return True  # If the loop completes without finding a mismatch, return True (it is a palindrome)


# Test cases
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"
string3 = " "

print(isPalindrome(string1))  # Output = True
print(isPalindrome(string2))  # Output = False
print(isPalindrome(string3))  # Output = True
