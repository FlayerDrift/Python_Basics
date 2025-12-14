"""
Problem 4: Two SumThis is the classic interview question.
Goal: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

Input: nums = [2, 7, 11, 15], target = 9Output: [0, 1] (Because nums[0] + nums[1] == 2 + 7 == 9)

Constraint: You cannot use the same element twice.
The "Brute Force" way would be to use two loops:"For every number x, check every other number y to see if x + y == target."But that is slow (O(n^2)).
The Hash Map Strategy:Instead of scanning ahead for the second number, what if we remembered what we have seen so far?As we iterate through the list, 
for each number num, we want to know: "Have I already seen the number target - num?"
"""


nums = [2, 7, 11, 15]
target = 13

def two_sum(nums, target):
    x = {}

    for i in range(len(nums)):
        find = target - nums[i]

        if find in x:
            return [x[find], i]
        
        x[nums[i]] = i


    return [] 

print(two_sum(nums, target))