"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
    # return a number that appears once from the array
    # for i, num in enumerate(nums):
        # count the number of times num appears
        # count = 0
        # for num2 in nums:
        #     if num2 == num:
        #         count += 1
    # if count = 1:
        #  return num

    # for num in nums:
    #     count = nums.count(num)
    #     if count == 1:
    #         return num

    counts = {} # O(1)
    for num in nums: # O(n)
        # count the number of times num appears
        if num not in counts: # O(1)
            # add the number to the dict
            counts[num] = 1
        else:
            counts[num] += 1

    # Loop over dict
    for key, value in counts.items():
        if value == 1:
            return key

print(single_number([3,3,2])) # 2
print(single_number([5,2,3,2,3])) # 5
print(single_number([10])) # 10