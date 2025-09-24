# LeetCode 49 : Group Anagrams
# Problem Link : https://leetcode.com/problems/group-anagrams/description/

def groupAnagrams(strs):
    res = {}  # Initialize an empty dictionary to store the sorted strings as keys and their list of anagram-variants as values.

    for s in strs:  # for every string in strs
        sorted_s = "".join(sorted(s))  # sort the string
        if sorted_s in res:  # If it exists in our result dictionary already,
            res[sorted_s].append(s)  # then append the anagram to its values.
        else:
            res[sorted_s] = [s]  # else, initialize it to the dictionary.

    return list(res.values())  # Return the groups of anagrams as lists, as required.


# Example
s1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(s1))  # Output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
