from typing import List
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Notes: 
    Time Complexity: 
        There are n digits and for each digit there are k characters on average. 
        So, for n digits, the total number of combination can be written as O(k^n)
        For each recursive call, we create a string of size m, the size of the
        string is proportional to the length of the digits, so we can say the length 
        of the string created is bounded by n 
        The overall time complexity is O(n.k^n), where n is the length 
        of the digits and k is the average characters represented by each digit.
    
    Space Complexity: 
        Creation of dictionary : O(1)
        Result list holds at most : K^n elements -> O(K^n)
        Recursive stack  -> O(n)
        Total space complexity : O(n.k^n)

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitsToChar = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl", 
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        result = []
        def backTracking(i, currString):
            if (len(currString) == len(digits)):
                result.append(currString)
                return
            for c in digitsToChar[digits[i]]:
                formedString = currString + c
                backTracking(i + 1, formedString)

        if digits:
            backTracking(0, "")
        
        return result


solution = Solution()
digits = "23"
print(solution.letterCombinations(digits))
