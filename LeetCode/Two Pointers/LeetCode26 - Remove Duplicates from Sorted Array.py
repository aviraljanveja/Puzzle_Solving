# LeetCode 26 : Remove Duplicates from Sorted Array
# Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):
    l = 1  # Left pointer to keep track of new elements
    r = 1  # Right pointer to iterate through the array

    while r < len(nums):  # Comparing adjacent elements, utilizing the fact that the array is already sorted.
        if nums[r] != nums[r-1]:  # Check if the current element is different from the previous one.
            nums[l] = nums[r]  # If yes, then a new element is found. Write it to the left-pointer position.
            l += 1  # Increment l, for storing the next unique element.
        r += 1  # Increment r

    return l  # After loop, Return l, which holds the number of unique elements in the array.


# Test case
arr1 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
solution1 = removeDuplicates(arr1)
print(solution1)  # Output: 3 (number of unique elements = 0, 1, 2)
