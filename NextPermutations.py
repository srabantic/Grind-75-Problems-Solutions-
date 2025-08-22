from typing import List
"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Notes:
Algorithm 
-> Iterate from the last elemnt in the list 
-> if you find a number less than the current 
-> reverse everything after that number
-> iterate again from that number to find the next number greater than the current 
-> swap them 

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def swap(self, nums, index1, index2):
        temp = nums[index2]
        nums[index2] = nums[index1]
        nums[index1] = temp

    def reverse(self, nums, begining, end):
        while begining < end:
            self.swap(nums, begining, end)
            begining += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        if len(nums) == 2:
            self.swap(nums, 0, 1)
        
        dec = len(nums) - 2
        # loop until dec >= 0 and we don't find a smaller number
        while dec >= 0 and nums[dec] > nums[dec + 1]:
            dec -= 1
        
        # After we find a smaller number
        # reverse everything after it
        self.reverse(nums, dec + 1, len(nums) - 1)

        # when dec = -1 meaning, we have gone over the entire list 
        # and the input does not have a lexicographical larger rearrangement
        # In this case, we rteurn the reversed list
        if dec == -1:
            return
        
        # After we find a smaller number
        # Iterate through the rest of the elements after it
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        
        # When we find the first number that is bigger than the number at dec index, swap the two
        self.swap(nums, next_num, dec)
        return nums

solution = Solution()
nums = [1,2,3]
nums1 = [3,2,1]
nums2= [1,1,5]
print(solution.nextPermutation(nums))
print(solution.nextPermutation(nums1))
print(solution.nextPermutation(nums2))