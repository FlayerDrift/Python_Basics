"""
Problem 7: Longest Substring Without Repeating Characters
Goal: Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb" Output: 3 (The answer is "abc", with length 3).
Input: s = "pwwkew" Output: 3 (The answer is "wke", with length 3). Note: "pwke" is wrong because 'w' repeats.
"""

# s = "pwwkew"
s = "abcabcbb"

def longest_substring(s):
    max_len = 0

    for i in range(len(s)):
        seen_list = []

        for j in range(i, len(s)):
            if s[j] in seen_list:
                break

            seen_list.append(s[j])
        
        max_len = max(max_len, len(seen_list))
    print(max_len)

longest_substring(s)