# LeetCode 344 : Reverse String
# Problem Link : https://leetcode.com/problems/reverse-string/description/

def reverseString(s):
    l = 0  # Left pointer at the start of the string
    r = len(s)-1  # Right pointer at the end of the string
    while l < r:  # Iterate only while l is less than r, as we need not move the middle character in an odd length string
        s[l], s[r] = s[r], s[l]  # Keep swapping the characters from the start and the end
        l += 1  # Increment the left pointer
        r -= 1  # Decrement the right pointer


# Test cases:
s1 = ['h', 'e', 'l', 'l', 'o']
reverseString(s1)
print(s1)  # Output = ['o', 'l', 'l', 'e', 'h']
