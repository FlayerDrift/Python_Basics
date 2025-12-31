class Solution:
    def romanToInt(self, s: str) -> int:
        """
        - Use a map to store the integer value of each Roman numeral.
        - Traverse the string from left to right, stopping at the second-last character.
        - For each character, compare it with the next one:
            • If the current value is smaller than the next value,
              subtract it (subtractive notation, e.g., IV, IX).
            • Otherwise, add it to the total.
        - The last character is always added because there is no next symbol
          to compare it with.
        - Return the accumulated total.
        """
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]

sol = Solution()
s = "III"
print(sol.romanToInt(s))