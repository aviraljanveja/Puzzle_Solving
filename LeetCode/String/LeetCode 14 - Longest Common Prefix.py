# LeetCode 14 : Longest Common Prefix
# Problem Link : https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    for i in range(len(strs[0])):   # Outer loop: iterate over each character of the first word
        for s in strs:  # Inner loop: For this character, Iterate over all words
            if i == len(s) or s[i] != strs[0][i]:  # Check if we have reached the end of the current word or found a mismatch
                return strs[0][:i]  # If either condition is true, return the first word till the current index as the longest common prefix

    return strs[0]  # If the loop completes without returning, then first word is the longest common prefix.

# Test Case
str1 = ["flower","flow","flowy"]
result = "".join(longestCommonPrefix(str1))
print(result)  # Output = "flow"

