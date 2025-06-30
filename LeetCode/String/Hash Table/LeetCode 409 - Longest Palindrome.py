# LeetCode 409 : Longest Palindrome
# Problem Link : https://leetcode.com/problems/longest-palindrome/description/

def longestPalindrome(s):
    seen = set()  # Initialize an empty set to check if the character appears odd or even number of times
    res = 0  # result variable to keep track of the maximum length of the palindrome

    for ch in s:  # Iterate through each character in the input string
        if ch in seen:  # If the character is repeating or even count like 2, 4, 6 ...
            seen.remove(ch)  # then we can remove it,
            res += 2  # and add 2 to our palindrome length.
        else:
            seen.add(ch)  # else, if the character is witnessed for the first time or odd count, we add it.

    # After the loop, If the set is not empty, we can add 1 to the result and return it.
    # This is done to account for that one odd character that can be placed in the middle of the palindrome.
    # For example : abcba
    if seen:
        res += 1

    return res


# The idea of a palindrome is to have balanced pairs of elements on both sides in a string,
# with one odd element that can be placed in the center, for example : abcba.
# In the above approach, the "unique elements only" property of the set is used to check
# if the count of elements is even or odd.

# Alternatively, a dictionary can be used above, but the set approach is more efficient as we
# do not really care for the exact count of the elements only, whether they are in exact pairs(even) or not (odd).


# Test case
s1 = "abccccdd"
print(longestPalindrome(s1))  # Output = 7

s2 = "a"
print(longestPalindrome(s2))  # Output = 1
