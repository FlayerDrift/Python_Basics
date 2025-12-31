from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        - Sort the list of strings lexicographically.
        - After sorting, the longest common prefix of all strings
          must be the common prefix of the first and last strings.
        - Compare characters of the first and last string index-by-index
          until a mismatch is found.
        - Return the substring up to the mismatch index.
        """
        
        new_list = sorted(strs)
        first = new_list[0]
        last = new_list[-1]
        for i in range(len(first)):
            if first[i] != last[i] or i == len(last):
                return first[0:i]


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))