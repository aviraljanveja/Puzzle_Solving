# LeetCode 977 : Squares of a Sorted Array
# Problem Link : https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sortedSquares(nums):
    res = []  # Initialize an empty list to store the squared values
    l = 0  # pointer 1 at the start of the list
    r = len(nums) - 1  # Pointer 2 at the end of the list

    while l <= r:  # Loop until the two pointers meet
        if abs(nums[l]) > abs(nums[r]) :  # Compare the absolute values at the left and right pointers
            res.append(nums[l] ** 2)  # If left is larger, append its square to the result list
            l += 1  # Move the left pointer one step towards right
        else:
            res.append(nums[r] ** 2)  # If right is larger or equal, append its square to the result list
            r -= 1  # Move the right pointer one step towards left

    return res[::-1]  # The resulting list is in descending order, so reverse before returning


# Test case
arr1 = [-4,-1,0,3,10]
print(sortedSquares(arr1))  # Output = [0, 1, 9, 16, 100]
