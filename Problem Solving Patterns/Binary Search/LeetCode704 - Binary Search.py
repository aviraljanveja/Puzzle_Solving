# LeetCode 704 : Binary Search
# Problem Link : https://leetcode.com/problems/binary-search/

def search(nums, target):  # Combination of Two Pointer + Divide & Conquer approaches

    # Two Pointer approach
    start = 0  # Initialize the "start" pointer at the beginning of the list
    end = len(nums) - 1  # Initialize the "end" pointer to the last index of the list

    # Loop runs as long as 'start' does not cross 'end'. This condition ensures we cover every element.
    while start <= end:

        # Divide & Conquer approach
        mid = (start + end) // 2  # Calculate the mid-point of the current search window

        if target == nums[mid]:  # Check if the target is found at 'mid'
            return mid  # If yes, return the index where 'target' is found

        elif target > nums[mid]:  # If the target is greater than nums[mid], only need to search the right half
            start = mid + 1  # Move 'start' to 'mid + 1' to narrow the search to the right half

        else:  # If the target is less than nums[mid], only need to search the left half
            end = mid - 1  # Move 'end' to 'mid - 1' to narrow the search to the left half

    # If the loop ends, without finding the required target
    return -1


# Test Case
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 0
print(search(nums1, target1))  # Output = 1
