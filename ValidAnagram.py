"""
Given two strings s and t, return true if it is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def isAnagram(self, s: str, t: str) -> bool:
        ## implementation with O(n)
        '''
        anagram = False

        for c in s:
            if ((len(s) == len(t)) and (t.count(c) == s.count(c))):
                anagram = True 
            else:
                return False 
        return anagram 
        '''

        ## Implementation with O(n)
        s_char_freq = {}
        t_char_freq = {}

        if (len(s) != len(t)):
            return False

        for char in s:
            s_char_freq[char] = s_char_freq.get(char, 0) + 1
        for char in t:
            t_char_freq[char] = t_char_freq.get(char, 0) + 1
        
        return s_char_freq == t_char_freq

        ## Another way to implement this is to use Python's Counter from Colections
        ## O(n) time complexity
    
        ## Implementation with O(n log n)
        '''
        s = sorted(s)
        t = sorted(t)
        return (s == t)
        '''
