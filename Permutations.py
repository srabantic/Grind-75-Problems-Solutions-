from typing import List
"""
Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Notes: 
    This is also a backtracking problem. 
    For each recursive call, we exclude the first element 
    and for each permutation list in perms, for every index (0, 1, 2, ...), 
    we add the missing element. 

    Time Complexity: O(n! * n) --- need to study more
    Space Complexity: O(n! * n)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(0, len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

nums = [1,2,3]
nums1 = [0,1]
solution = Solution()
print(solution.permute(nums))
print(solution.permute(nums1))