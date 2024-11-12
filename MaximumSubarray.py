from typing import List
"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 2
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_local = max_global = nums[0]

        for i in range(1, len(nums)):
            max_sum = max_local + nums[i]
            if (max_sum > nums[i]):
                max_local = max_sum
            else:
                max_local = nums[i]
            
            max_global = max(max_local, max_global)
        return max_global

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [1]
nums2 = [5,4,-1,7,8]
solution = Solution()
print(solution.maxSubArray(nums))
print(solution.maxSubArray(nums1))
print(solution.maxSubArray(nums2))
