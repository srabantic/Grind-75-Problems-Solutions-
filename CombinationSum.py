from typing import List
"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Notes:
Use backtracking to solve this problem
In the implementation we add a copy of the current list to the result array. That is because lists in 
python are reference type, so it stores a reference and it values. Hence if the curr list changes 
at any point in the future, the stored list in result will also change. That's why we create 
a copy so that we store an exact copy of the curr list at that time.

Time Complexity: O(n^(T/min_candidate)), all the recursive calls will be bounded by this because 
the maximum recursive call will be with the smallest candidate. n is the number of candidates and T is the target.

Space Complexity: O(T/min_candidate)) + O(output_size)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return 
                
                curr.append(candidates[j])
                dfs(j, curr, total + candidates[j])
                curr.pop()
        dfs(0, [], 0)
        return res

solution = Solution()
candidates = [2,3,6,7]
target = 7
print(solution.combinationSum(candidates, target))