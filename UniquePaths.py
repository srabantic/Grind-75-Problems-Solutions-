"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
class Solution:
    """
    In this solution- 
    -> we create a matrix with one more row and colum than that is given to us, so (m + 1), (n+ 1)
        -> We fill the entire mattix with 0
        -> We take one more row and colum to make our calculation easy as we calculate 
            the current rows value by dp[i + 1][j] + dp[i][j+1]
    -> If we didn't take one extra row and colum, we would fo out of bound for 
        calculating boundary values
    -> Time Complexity : O(m * n)
    -> Space Complexity : O(m * n)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(0, m + 1):
            dp.append([0] * (n + 1))
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][ j + 1]
        return dp[0][0]


solution = Solution()
m = 3
n = 7
print(solution.uniquePaths(m, n))