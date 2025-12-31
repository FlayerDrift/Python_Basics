from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - Traverse the array once while storing numbers we have seen in a hash map.
        - For each number, compute the complement needed to reach the target.
        - If the complement already exists in the hash map, we have found the pair.
        - Return the indices of the complement and the current number.
        - This avoids the O(n²) brute-force approach and runs in O(n) time.
        """
        
        hash_list = {}
        for _idx, value in enumerate(nums):
            x = target - value
            if x in hash_list:
                return [hash_list[x], _idx]

            hash_list[value] = _idx
            
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))