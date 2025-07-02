# LeetCode 217 : Contains Duplicate
# Problem Link : https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums):
    check = set()  # Initialize an empty set to keep track of numbers we have seen so far.

    for n in nums:  # Iterate through the array.
        if n in check:  # Check if the current number is already in the array.
            return True  # If it is, we have found a duplicate, so return True.
        else:
            check.add(n)  # else, add the current number to the set.

    return False  # If the loop exits without finding any duplicates, return False.


# Test Case:
nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))  # Output : True
