"""
Problem 3: Move Zeroes

This problem introduces a variation of the Two Pointer technique often called "Fast and Slow Pointers."
Goal: Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. 
Constraint: You must do this in-place without making a copy of the array.

Input: nums = [0, 1, 0, 3, 12] Output: [1, 3, 12, 0, 0]

The Logic: Instead of a pointer at the start and end, imagine two pointers starting at the beginning:
Iterator (Fast): Scans through every element.
Placeholder (Slow): Keeps track of the position where the next non-zero element should go.
"""

nums = [0, 1, 0, 3, 12]

def move_zeros(nums):
    slow = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[slow] , nums[i] = nums[i], nums[slow]
            slow += 1

    return  nums

print(move_zeros(nums))