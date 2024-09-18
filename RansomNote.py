"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(magazine) < len(ransomNote)):
            return False 

        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1) # node that the last parameter passed is the count of how many replacements we want to make at once 
            else:
                return False 
        return True

solution = Solution()
randomNode = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
print(solution.canConstruct(randomNode, magazine))

                