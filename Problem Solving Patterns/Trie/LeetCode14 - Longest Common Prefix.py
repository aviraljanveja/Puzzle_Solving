# LeetCode 14 : Longest Common Prefix
# Problem Link : https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    for i in range(len(strs[0])):  # We pick the first string from the list of strings and check if its characters,
        for s in strs:  # match across the rest of the strings in the list.
            if i == len(s) or strs[0][i] != s[i]:  # As soon as some string length is reached, or we find a character mismatch,
                return strs[0][:i]  # we return the slice of the first string upto the matching character length "i" as our common prefix

    return strs[0]  # If all characters of the first string are common across all strings, then it naturally becomes our longest common prefix


# Test Cases :
str1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(str1))  # Output = "fl"

str2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(str2))  # Output = ""
