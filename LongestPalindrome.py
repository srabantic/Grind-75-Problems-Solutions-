"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

NOTE: To create a palindrome, we need to have 1 odd characters and all characters must be even. 
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_chars = {}
        length = 0
        odd_found = False

        for c in s:
            count_chars[c] = count_chars.get(c, 0) + 1

        for count in count_chars.values():
            length += (count // 2) * 2
            if count // 2 == 1:
                odd_found = True 
        return length + (1 if odd_found else 0)

s = "abccccdd"
solution = Solution()
print(solution.longestPalindrome(s))
print(solution.longestPalindrome.__annotations__) #annotations 
        


    
