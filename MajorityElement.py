from typing import List
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Note: Inserting n element in the dictionary takes O(n) space complexity. 
Time Complexity for both approaches is O(n) since we are looping over the the given list in both approaches.
"""

class Solution:

    # Solution with Hash Map 
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxCount:
                res = n 
            maxCount = max(count[n], maxCount)
        return res
    
    # Solution with Boyer Moore Algorithm 0(1) Space Complexity 
    def majorityElementOptimal(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n 
            count += (1 if n == res else -1)
        return res
        

nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))
print(solution.majorityElementOptimal(nums))


        

