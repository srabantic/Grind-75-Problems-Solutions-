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
### the above solution is correct but it uses extra time and memory because 
## we are using string concatination and in python strings are immutable. 
# So, everytime, we contatinate the string, it creates a new string.

"""
The solution below uses two pointers and has time complexity O(n) and 
space compleixity O(1)
"""
def isPalindrome2(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if (s[i].lower() != s[j].lower()):
            return False
        i += 1
        j -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
t = "A am a cat"
print(isPalindrome(t))