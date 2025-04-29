from typing import List
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Notes:
    We use two pointer approach to solve this. 
    Time complexity: O(n)
    Space complexity: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            w = right - left 
            l = min(height[right], height[left])
            area = w * l
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area

solution = Solution()
height_1 = [1,8,6,2,5,4,8,3,7]
height_2 = [1,1]
print(solution.maxArea(height_1))
print(solution.maxArea(height_2))