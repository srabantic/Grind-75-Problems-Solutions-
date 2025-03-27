"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Example 2:

Input: s = " -042"

Output: -42

Example 3:

Input: s = "1337c0d3"

Output: 1337

Example 4:

Input: s = "0-1"

Output: 0

Example 5:

Input: s = "words and 987"

Output: 0

"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        result = 0
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            

        while (i < len(s)):
            digit_value = ord(s[i]) - ord('0')
            if not (digit_value >= 0 and digit_value <= 9):
                break
            else:
                result = result * 10 + digit_value
                if (result * sign) < -2**31:
                    return  -2**31
                elif (result * sign) > 2**31 - 1:
                    return 2**31 - 1
            i += 1

        return result * sign
    
        
solution = Solution()
s = "42"
print(solution.myAtoi(s))
s = " -042"
print(solution.myAtoi(s))