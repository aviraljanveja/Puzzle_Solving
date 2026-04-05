# LeetCode 27 : Remove Element
# Problem Link : https://leetcode.com/problems/remove-element/description/

def removeElement(nums, val):
    l = 0  # Left pointer to keep track of non-val elements
    r = 0  # Right pointer to iterate through the array

    while r < len(nums):  # Iterate through the array
        if nums[r] != val:  # If the current element is not equal to val,
            nums[l], nums[r] = nums[r], nums[l]  # swap it to the current position of the left pointer
            l += 1  # Increment l, to store the next non-val element

        r += 1  # Check the next element

    return l  # After the loop, we return l, which now holds the number of non-val elements in the array


# Test Cases :
nums1 = [3, 2, 2, 3]
val1 = 3
print(removeElement(nums1, val1))  # Output = 2

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
print(removeElement(nums2, val2))  # Output = 5
