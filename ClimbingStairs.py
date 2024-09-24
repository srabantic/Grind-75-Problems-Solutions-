"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

NOTES: 
This problem is same as the Fibonacci sequence. If we solve this using recursion, we see that 
we have to make duplicate calls with the same input, which gives us O(2^n) time complexity.

We use a caching technique called memoization to solve this problem, where we store the
result so we do not need to make duplicate calls - O(n) time complexity.

This solution also follows the bottom-up approach of Dynamic Programming 
where we start from the given input and make our way to 0. 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        total_ways = 0

        if ( n == 1 ): #edge/base case 
            return 1

        while (n - 2 >= 0):
            total_ways = a + b
            a = b
            b = total_ways 
            n -=1
        return total_ways

n = 10
s = Solution()
print(s.climbStairs(n))
            
