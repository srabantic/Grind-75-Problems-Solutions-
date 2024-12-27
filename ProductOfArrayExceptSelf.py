from typing import List
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Note: We use prefix-postfix method to solve this 
Time Complexity : O(n)
Space Complexity : O(1), note that the problem says that output array is not counted 
                    for space complexity. 

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1

        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range (len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

solution = Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))

        