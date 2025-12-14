"""
Goal: Write a function that reverses a list of characters.Input: s = ["h", "e", "l", "l", "o"]Output: ["o", "l", "l", "e", "h"]
Constraint: You must modify the input list directly (in-place) with BigO(1) extra memory. 
Do not define a new list.To do this efficiently in Python, we use the Two Pointer approach again (start and end), swapping characters as we move toward the middle.
There is a specific Python syntax that lets you swap two values a and b in a single line without using a temporary variable.
"""

s = ["h", "e", "l", "l", "o"]

def reverse_char_list(s):
    n = len(s)
    for i in range(n // 2):
        s[i], s[-1 - i] = s[-1 - i], s[i]

    return s

print(reverse_char_list(s))