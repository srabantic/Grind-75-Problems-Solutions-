from typing import List
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

"""
class Solution:
    ## Solution using a stack
    # Time complexity : O(n+m)
    # Space complexity : O(n + m )
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack  = []
        t_stack = []
        for char in s:
            if (char == "#" and s_stack):
                s_stack.pop()
            elif(char != "#"):
                s_stack.append(char)
        for char in t:
            if (char == "#" and t_stack):
                t_stack.pop()
            elif(char != "#"):
                t_stack.append(char)
        return s_stack == t_stack
    
    # A more cleaner approach 
    # Please note that the time and space complexity will remain same as approach 1
    def backspaceCompare2(self, s: str, t: str) -> bool:

        s_stack  = []
        t_stack = []

        def str_compare(comapre_string : str, stack : list):
            for char in comapre_string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
                
        str_compare(s, s_stack)
        str_compare(t, t_stack)
        return s_stack == t_stack

    # Solution with O(1) space complexity 
    def backspaceCompare3(self, s: str, t: str) -> bool: 
        """
        Algorithm:
        1. Start indexing  both s and t from the last index (going backwards)
        2. Call the helper function on both index
        3. If i and j are both >= 0 and if the chars at both index do not match, then return False
        4. If either index i or j is out of bound (<0), then return False because one string has more chars than 
            the other.
        5. Decrement i and j 
        6. If step 3 and 4 are not True, then return True 
        """
        def get_valid_char_index(str, index):

            """
            This function take checks and returns the index on a valid char.
            Algorithm:
                1. If we encounter a "#", we increment skip to 1 (that menas the next char has to be removed)
                2. If char is not "#" and skip is > 0, then we decrement skip because the current char will be erased.
                3. If skip is 0 and char is not "#", then we return the index because 
                    it is a valid char.
                4. Decrement inced because we are doing from right to left (backwords)
                5. If a valid char is not found, return -1.
            """
            
            skip_char = 0
            while index >= 0:
                if (str[index] == "#"):
                    skip_char +=1
                elif (skip_char > 0): 
                    skip_char -= 1
                else:
                    return index
                index -=1
            return -1
    
        i, j = len(s) -1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_valid_char_index(s, i)
            j = get_valid_char_index(t, j)

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0) != (j>=0):
                return False
            
            i -=1
            j -=1

        return True



s = "ab#c"
t = "ad#c"
solution = Solution()
print(solution.backspaceCompare3(s, t))

s = "ab##"
t = "c#d#"
print(solution.backspaceCompare3(s, t))

s = "a#c"
t = "b"
print(solution.backspaceCompare3(s, t))

s = "y#fo##f"
t = "y#f#o##f"

print(solution.backspaceCompare3(s, t))

s ="bbbextm"
t ="bbb#extm"

print(solution.backspaceCompare3(s, t))

