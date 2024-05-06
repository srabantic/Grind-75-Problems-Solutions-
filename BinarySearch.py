"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""
def search(self, nums: List[int], target: int) -> int:
        ## Implementation with O(n) time complexity
        ''' 
        if target in nums:
            return nums.index(target)
        else:
            return -1
        '''
        
        ## Implementation with O(log n) time complexity
        start, end = 0, len(nums) -  1
        while start <= end:
            mid = start + (end - start) // 2
            if (nums[mid] == target):
                return mid 
            elif (nums[mid] > target):
                end = mid - 1 
            else:
                start = mid + 1 
        return -1
  
