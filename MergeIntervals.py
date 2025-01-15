from typing import List
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Note: 
    Time Complexity : O(n log n)
    Space Complexity : O(n)

    Note that .sort uses TimSort which takes an auxiliary space of O(n). 
    the result_intervals array in the worst case (no overlapping intervals) will need 
    to store n intervals given. 
    So, the overall space complexity is O(n).

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the array 
        intervals.sort(key = lambda x: x[0])
        result_intervals = [intervals[0]]

        for start, end in intervals[1:]:
            result_interval_end = result_intervals[-1][1]
            if start <= result_interval_end:
                result_intervals[-1][1] = max(result_intervals[-1][1], end)
            else:
                result_intervals.append([start, end])
        print (result_intervals)
        return result_intervals


        

solution = Solution()
intervals = [[1,3],[8,10],[15,18],[2,6]]
solution.merge(intervals)