"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        forward_string = ''
        backward_string = ''
        i = 0
        j = len(s) - 1
        while (i < len(s) and j >= 0):
            if (s[i].isalnum() and s[i] != ""):
                forward_string += s[i]
            if (s[j].isalnum() and s[j] != ""):
                backward_string += s[j]
            i= i + 1
            j = j - 1

        return (forward_string == backward_string)
