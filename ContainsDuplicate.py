from typing import List
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_hashset = set()
        for n in nums:
            if n in duplicate_hashset:
                return True
            duplicate_hashset.add(n)
        return False
        
list1 = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(list1))

list2 = [1,2,3,4]
print(solution.containsDuplicate(list2))



