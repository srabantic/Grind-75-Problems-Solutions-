from typing import List
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1: 
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Time Complexity : O(n * m)
Space Complexity : O(1) -> if we do not count the result array
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        result = []

        while left < right and top < bottom:
            # left to right 
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # top right to bottom right 
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # bottom right to left 
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # bottom left to top left 
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result


solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix))
