from typing import List
from collections import deque
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Time complexity : O(rows * cols)
Space complexity : O(rows * cols)

To do: Take a look at how to solve this problem using dfs(recursive approach)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ilands = 0


        def bfs(r, c):
            queue = deque()
            directions_map = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions_map:
                    new_dr = row + dr
                    new_col = col + dc

                    if (0 <= new_dr < rows and 0 <= new_col < cols):
                        if grid[new_dr][new_col] == "1" and (new_dr, new_col) not in visited:
                            queue.append((new_dr, new_col))
                            visited.add((new_dr, new_col))
        
        for row in  range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    ilands += 1
        return ilands 
    

    
solution = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid))

grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid1))