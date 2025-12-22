"""
Problem 8: Valid Parentheses
Goal: Given a string s containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

A string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}" Output: True
Input: s = "(]" Output: False (Mismatched types)
Input: s = "([)]" Output: False (Wrong closing order — [ must close before ()
"""

# s = "()[]{}"
# s = "(]"
s = "([)]"

def isValid(s):
    stack = []
    mapping = {")": "(", 
               "}": "{", 
               "]": "["}

    for i in s:
        if i in mapping:

            if stack and stack[-1] == mapping[i]:
                stack.pop()
            else:
                return False
            
        else:
            stack.append(i)
    
    if not stack:
        return True
    else:
        return False

print(isValid(s))