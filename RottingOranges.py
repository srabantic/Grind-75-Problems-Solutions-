from typing import List
import collections
"""
ou are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Note: 
    This problem differs slightly from the implementation of number of ilands, though both 
    problems use BFS.

    Here we do not need a visited set because the grid itself can act as one, 
    everytime we see a fresh orange, we make it rotten (== 2), this tells us 
    that this cell has been visited and we do not process it any more.

    We also have a variable called fresh because we need to keep track of 
    the fresh oranges, if it is not possible for us to make all oranges 
    rotten, then we need to return -1, that's why we need to keep track of 
    the fresh oranges.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        num_minutes = 0
        queue = collections.deque()
        directions_map = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == 1):
                    fresh += 1
                if (grid[row][col] == 2):
                    queue.append((row, col))
        
        if fresh == 0:
            return 0

        while queue and fresh > 0:
            # NOTE: The following loop ensures that we simultaniously take care 
            #       of all the rotten oranges at one time 
            for i in range(len(queue)): 
                row, col = queue.popleft()
                for dr, dc in directions_map:
                    new_dr = row + dr
                    new_dc = col + dc 
                    if (0 <= new_dr < rows and 0 <= new_dc < cols):
                        if (grid[new_dr][new_dc] == 1):
                            grid[new_dr][new_dc] = 2
                            queue.append((new_dr, new_dc))
                            fresh -= 1
            num_minutes += 1
        return num_minutes if fresh == 0 else -1


solution = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(solution.orangesRotting(grid))

grid1 = grid = [[2,1,1],[0,1,1],[1,0,1]]
print(solution.orangesRotting(grid1))

grid2 = [[0,2]]
print(solution.orangesRotting(grid2))
