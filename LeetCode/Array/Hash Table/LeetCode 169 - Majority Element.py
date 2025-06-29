# LeetCode 169 : Majority Element
# Problem Link : https://leetcode.com/problems/majority-element/description/

def majorityElement(nums):
    # The Boyer-Moore Majority Voting Algorithm
    # This algorithm finds the majority element in an array by leveraging
    # the fact that a majority element exists, that appears more than n/2 times.

    key = None  # Initialize a key
    count = 0  # Initialize count to 0

    for num in nums:  # Traverse the array
        if count == 0:  # Whenever the count gets to 0, update the key
            key = num

        if num == key:  # Increment the count by 1, if the element repeats
            count += 1
        else:  # Decrement the count by 1, otherwise
            count -= 1

    return key  # If there is a majority element in the array, it is guaranteed to
    # survive the above voting process and hence, we return it as our final key.



    # The straight forward approach : Using a dictionary to store element counts.
    # count = {}  # Initialize an empty dictionary to store the count of each element
    #
    # for num in nums:  # As the array is traversed, the dictionary is updated to store the count of each element.
    #     if num in count:  # If the element is already in the dictionary, increment its count
    #         count[num] += 1
    #     else:
    #         count[num] = 1  # If the element is not in the dictionary, store it and initialize its count to 1
    #
    #     if count[num] > len(nums) / 2:  # Check if any element's count is already greater than n / 2
    #         return num  # If yes, then we can return it without having to traverse through the rest of the array


# Test case
list1 = [2,2,1,1,1,2,2]
print(majorityElement(list1))  # Output = 2
