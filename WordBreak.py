from typing import List
"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Notes:
    Time Complexity:
        O(n) -> n is the length of the string 
        O(m) -> m is the length of the word dicts array
        O(t) -> t is the length of the maximum word in the word dicts array
    
    Space Complexity:
        O(n) -> n is the length of the string, as we create len(s) + 1 elements in the dp array for storage
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if((i + len(w) <= len(s)) and (s[i : i + len(w)] == w)):
                    dp[i] = dp[i + len(w)]

                    if dp[i]:
                        break
        return dp[0]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
solution = Solution()
print(solution.wordBreak(s, wordDict))


