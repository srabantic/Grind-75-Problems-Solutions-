"""
Given a string s, find the length of the longest 
substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Notes: 
    We are using the sliding window approach with two pointer here
    Everytime we see a dupliocated value, we remove it from and everything before it from the set (this
        ensures contiguousness and uniqueness)
    we are using a set here because set ensures that all elements are unique.  
    Insertation and deletion in a set takes O(1) time complexity.

    Time Complexity : 
        -> To go over the entire alg, the for loop runs O(n) times as we need 
            to traverse through the string
        -> The while loop runs at most O(n) times for the entire alg because 
           each char is being removed exactly 1 time.
        -> The while loop does not run n times for each iteration of the 
           for loop.
        -> Hense, the total time complexity of the alg is O(n)
    
    Space Complexity : 
        -> The space complexity is determined by the charSet, which can hold up to 
            k unique chars or n in worst case scenarioes where all chars are unique. 
        -> Space complexity : O(k), where is the size of the char set.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        l = 0

        for r in range(0, len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result
    
solution = Solution()

s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))
s = s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))
s = "bbbbb"
print(solution.lengthOfLongestSubstring(s))



        