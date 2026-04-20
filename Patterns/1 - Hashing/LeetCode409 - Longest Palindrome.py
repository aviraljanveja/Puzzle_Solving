# LeetCode 409 : Longest Palindrome
# Problem Link : https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s):
    seen = set()  # Initialize an empty set to check for odd / even count of characters
    length = 0

    for ch in s:
        if ch in seen:  # If an element repeats,
            seen.remove(ch)  # remove it, since we just formed a pair.
            length += 2  # Each pair contributes 2 characters to the palindrome length
        else:
            seen.add(ch)  # else, add it to the set

    if seen:  # If there is any leftover character (odd count),
        length += 1  # we can put one of them in the center, while maintaining the palindrome, so add 1 to length.

    return length  # Return final length value of the longest possible palindrome, that can be constructed from the given string.


# Test Cases :
s1 = "abccccdd"
print(longestPalindrome(s1))  # Output = 7

s2 = "a"
print(longestPalindrome(s2))  # Output = 1
