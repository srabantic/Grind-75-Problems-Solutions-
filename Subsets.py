from typing import List
"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Notes: 
    If the input has n elements, there are 2^n possible subsets, because each element can either be included in a subset or not.
    Time Complexity: 
        For n elements in the list, there are 2^n possible subsets because each element 
        have the choice of being chosen or not. 
        Each subset can vary in size from 0 to n. 
        Hence, the total timecomplexity is O(2^n . n)
    Space Complexity:
        Since we process each element in the list once before backtracking, the size 
        of the recursive stack is at most O(n) (if we consider the path where we add all elemtns to the subset)
        The result list can contain 2^n subsets, each with size of at most n 
        Therefore, the overall space complexity is O(2^n . n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subsets = []

        def dfs(i):
            if i >= len(nums):
                result.append(subsets.copy())
                return 

            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return result
    
nums = [ 1, 2, 3]
solution = Solution()
print(solution.subsets(nums))