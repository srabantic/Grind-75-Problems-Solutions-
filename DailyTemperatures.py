from typing import List
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Notes: 
    Time Complexity : O(n)
    Space Complexity : O(n) -> including the output array
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_array = [0] * len(temperatures)
        stack_array = []

        for i in range(len(temperatures)):
            while stack_array and temperatures[i] > stack_array[-1][0]:
                indx = stack_array.pop()[1]
                output_array[indx] = i - indx
            stack_array.append((temperatures[i], i))
        return output_array

solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))


