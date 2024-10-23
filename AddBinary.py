"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        total, carry = 0, 0

        # we are reverting the strings here because we start adding from the rightmost side

        a, b = a[::-1], b[::-1] 
        for i in range(max(len(a), len(b))):
            # we can also use int(a[i]) to get the int value
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digitA + digitB + carry 
            char = str(total % 2) # takes the remainder
            res = char + res
            carry = total // 2 # takes the quotient
        
        if carry:
            res = "1" + res
    
        return res

solution = Solution()
a = "11"
b = "1"
print(solution.addBinary(a, b))
a = "1010"
b = "1011"
print(solution.addBinary(a, b))
