"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Notes:
    Time Complexity : 
        The outer loop runs O(n) times
        The inner loop is bounded by O(n) operaitons 
        The total complexity is O(n^2)
    
    Space Complexity : O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultLength = 0
        resultIndex = 0 

        def determine_palindrome(l, r):
            nonlocal resultIndex, resultLength
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resultLength):
                    resultIndex = l
                    resultLength = r - l + 1
                
                l -= 1
                r += 1

        for i in range(len(s)):

            # Odd length palindrome 
            l = i
            r = i
            determine_palindrome(l, r)

            # Even length palindrome
            l = i
            r = i + 1
            determine_palindrome(l, r)
        
        return s[resultIndex : resultIndex + resultLength]

solution = Solution()
s = "babad"
print(solution.longestPalindrome(s))



