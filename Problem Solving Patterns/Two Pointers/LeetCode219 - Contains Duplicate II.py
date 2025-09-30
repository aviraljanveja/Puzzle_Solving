# LeetCode 219 : Contains Duplicate II
# Problem Link : https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums, k):
        seen = set()  # Initialize an empty set
        l = 0  # Left Pointer
        r = 0  # Right Pointer

        while r < len(nums):
            if r - l > k:  # First check if the gap between element indices is at most k
                seen.remove(nums[l])
                l += 1

            if nums[r] in seen:  # If duplicate found within k indices, return True
                return True
            else:
                seen.add(nums[r])  # Else, add current element to the set

            r += 1  # Increment right pointer of the loop

        return False  # If loop exits without finding a duplicate within k indices, return False.


# Test Cases :
nums1 = [1,2,3,1]
k1 = 3
print(containsNearbyDuplicate(nums1, k1))  # Output = True

nums2 = [1,0,1,1]
k2 = 1
print(containsNearbyDuplicate(nums2, k2))  # Output = True

nums3 = [1,2,3,1,2,3]
k3 = 2
print(containsNearbyDuplicate(nums3, k3))  # Output = False
