"""
Problem 5: Valid Anagram

Goal: Given two strings s and t, return True if t is an anagram of s, and False otherwise.
Definition: An Anagram is a word formed by rearranging the letters of another word (e.g., "listen" -> "silent"). Essentially, do they have the exact same characters with the exact same counts?

Input 1: s = "anagram", t = "nagaram" Output: True
Input 2: s = "rat", t = "car" Output: False (Different letters: 'r', 'a', 't' vs 'c', 'a', 'r')

Strategy Hint: If you count how many times 'a' appears in string s, it should match the count of 'a' in string t.
How would you use a dictionary (or two) to solve this?
"""

s = "anagram"
t = "nagaram"

def valid_anagram(s, t):

    if len(s) != len(t):
        return False
    
    first = {}
    for i in s:
        first[i] = first.get(i, 0) + 1

    second = {}
    for j in t:
        second[j] = second.get(j, 0) + 1

    return first == second

print(valid_anagram(s, t))