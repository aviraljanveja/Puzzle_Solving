# LeetCode 1 : Two Sum 
# Problem Link : https://leetcode.com/problems/two-sum/description/

def twosum(nums, target):
    check = {}  # Step 1: Create an empty dictionary to store array numbers as keys and their indices as values

    for i in range(len(nums)):  # Step 2: Iterate through the array
        complement = target - nums[i]  # Step 3: Calculate the complement
        if complement in check:  # Step 4: Check if the complement already exists in the dictionary
            return [check[complement], i]  # Step 5: If yes, return the indices of the complement and the current number

        check[nums[i]] = i  # Step 6: Store the current number as key and its index as value in the dictionary


list1 = [11, 2, 7, 15]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)  # Output : [1, 2]


# Brute force solution using the selection-sort mechanism :
# def twosum(nums, target):
#     for i in range(len(nums) - 1):  # Outer loop to pick the first number
#         for j in range(i+1, len(nums)):  # Inner loop to pick the second number, starting after the first
#             if nums[i] + nums[j] == target:  # Check if the two numbers sum up to target
#                 return [i,j]  # If condition is met, return their indices
#
#
# list1 = [2,11,15,7]  # Given list
# target1 = 9  # Target integer
#
# solution = twosum(list1, target1)
# print(solution)  # Output : [0, 3]
