# LeetCode 1 : Two Sum 
# Problem Link : https://leetcode.com/problems/two-sum/description/

def twosum(nums, target):
    check = {}  # Initialize an empty dictionary

    for i in range(len(nums)):  #  Iterate through the array
        complement = target - nums[i]  # Calculate the complement
        if complement in check:  # If the complement already exists in the dictionary
            return [check[complement], i]  # then return the indices of the complement and the current number

        check[nums[i]] = i  # Else, Store the current number as key and its index as value in the dictionary


list1 = [11, 2, 7, 15]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)  # Output : [1, 2]
