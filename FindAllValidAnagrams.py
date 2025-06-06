from typing import List
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Notes:
 Time Complexity : O(s)
 Space Complexity : O(n) -> including the result list
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        result = []

        p_char_count = {}
        s_char_count = {}

        if (len(s) < len(p)):
            return result

        for char in p:
            p_char_count[char] = p_char_count.get(char, 0) + 1
        
        for right in range(0, len(s)):
            s_char_count[s[right]] = s_char_count.get(s[right], 0) + 1

            if (right - left + 1 > len(p)):
                s_char_count[s[left]] -= 1
                if s_char_count[s[left]] == 0:
                    s_char_count.pop(s[left])
                left += 1
        
            if (p_char_count == s_char_count):
                result.append(left)

        return result


s = "cbaebabacd"
p = "abc"
solution = Solution()
print(solution.findAnagrams(s, p))

s = "abab"
p = "ab"
print(solution.findAnagrams(s, p))
