"""

Problem 1: Valid Palindrome

Goal: Write a function that returns True if a string is a palindrome (reads the same forwards and backwards) and False if it isn't. 
Constraint: Do not use the shortcut s[::-1]. We want to check the characters manually.
To solve this efficiently, we usually compare the characters at the start of the string with the characters at the end.
If you have the string s = "racecar", what Python code would you write to access the first letter and the last letter?

"""

s = "abba"
s_list = list(s)

def check_palindrom(s_list):
    x = 1
    for i in range(0, len(s_list)):
        start = s_list[i]
        end = s_list[len(s_list) - x]

        if start != end:
            return False
        
        x += 1

    return True
    
print("The string is a palindrome" if check_palindrom(s_list) else "The string is not a palindrome")

# ==================================================================================================
# Better answer
# ==================================================================================================

"""
We only need to check half of the string and no need turn the string into list
"""

def check_palindrom_2(s):
    n = len(s)
    
    for i in range(n // 2):

        if s[i] != s[-1 - i]:
            return False
    
    return True

print("The string is a palindrome" if check_palindrom_2(s) else "The string is not a palindrome")