# LeetCode 242 : Valid Anagram
# Problem Link : https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s, t):
    if len(s) != len(t):  # Check for equal length as the first test
        return False

    def dictmaker(arr):  # Helper function to convert a string into a dictionary with character counts
        d = {}  # Initialize an empty dictionary
        for i in arr:  # Iterate over characters
            if i in d:  # If the character is already in the dictionary, increment its count value
                d[i] += 1
            else:  # else, add it to dictionary
                d[i] = 1
        return d  # Return the formed dictionary


    # Compare the dictionaries generated from both strings
    return dictmaker(s) == dictmaker(t)  # If they are equal, the strings are anagrams


# Test cases
s1 = "anagram"
t1 = "nagaram"
print(isAnagram(s1, t1))  # Output = True

s2 = "rat"
t2 = "car"
print(isAnagram(s2, t2))  # Output = False
