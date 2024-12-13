from collections import deque
from typing import List
"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Note:
    Time Complexity 
        - O(n * m), n = number of rows, m = number of cols 
    Space Complexity
        - O (n * m), the queue can hold at most n*m number of rows and cols
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # we will use a deque for this 
        queue = deque()

        # define row and col 
        rows = len(mat)
        cols = len(mat[0])

        # manipulate the matrix 
        # append the cell (row, col) which has a 0 in the queue 
        # manipulate the cell entries with inf which has an 1 in them
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = float('inf')

        # there are four possible ways we can navigate from a cell 
        # up, down, right, left
        # we will have a list to hold this four positions 
        directions_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # we will loop until there are elements in the queue 
        while queue:
            # pop the first cell that we entered in the queue 
            r, c = queue.popleft()

            # loop through all the directions in the direction map
            for dr, dc in directions_map:
                # we add the directions to the original row and col
                # for each direction, we compare the value with the original cell
                # of the value in the original cell is > 1 (meaning inf)
                # then we update the distance on that cell to be one.
                new_dr = r + dr
                new_dc = c + dc 

                if (0 <= new_dr < rows and 0 <= new_dc < cols):
                    if (mat[new_dr][new_dc] > mat[r][c] + 1):
                        mat[new_dr][new_dc] = mat[r][c] + 1
                        queue.append((new_dr, new_dc))
        return mat
                    
 
s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))