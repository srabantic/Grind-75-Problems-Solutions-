from typing import List
"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Note:
    Time Complexity: O(n * target)
        The outer loop traverses each element in the given array ->o(n)
        the inner loop traverses each element int the dp hashset, which can 
        conrain at most target = sum(nums)// 2 elements

    Space Complexity: O(target)
        dp can conatin at most target element and nextDp is bounded by the 
        size of dp
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
 
            for element in dp:
                totalSum = element + nums[i]
                if totalSum == target:
                    return True
                nextDp.add(totalSum)
                nextDp.add(element)

            dp = nextDp
        return False

solution = Solution()
nums = [1, 5, 11, 5]
print(solution.canPartition(nums))

nums = [1, 2, 3, 5]
print(solution.canPartition(nums))



