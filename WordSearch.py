"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Notes:
    Time Complexity : O(m * 4^n), m = number of cells in the board, n = length of word
    Space Complexity : O(n)
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if (i == len(word)):
                return True
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
                return False
            
            visited.add((r, c))
            result = (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))
            return result
        
        for r in range(rows):
            for c in range (cols):
                if dfs(r, c, 0):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

solution = Solution()
print(solution.exist(board, word))