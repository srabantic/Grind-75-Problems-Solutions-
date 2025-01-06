from typing import List
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            # check if left part of the array is sorted 
            if (nums[low] <= nums[mid]):
                # now check if the target is present within this range 
                if (nums[low] <= target < nums[mid]):
                    # then the target is in the left half, update right pointer 
                    high = mid - 1
                else:
                    # otherwise, it is in the right half, update left pointer
                    low = mid + 1
            
            # Check if the right part of the array is sorted 
            else:
                # now check if the target is present within this range 
                if (nums[mid] < target <= nums[high]):
                    # then the target is in the right half, update left pointer
                    low= mid + 1
                else:
                    # otherwise, taget is in the left half, update right pointer 
                    high = mid - 1
        return -1 



    

solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))

nums1 = [4,5,6,7,0,1,2]
target1 = 3
print(solution.search(nums1, target1))

nums2 = [1]
target2 = 0
print(solution.search(nums2, target2))
