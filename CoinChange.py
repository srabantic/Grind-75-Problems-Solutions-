from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Note: 
    This is a dynamic programming problem. 
    We will be using the bottom up approach to solve this problem 
    We go from dp[0] -> dp[amount], we know that dp[0] will be 0 since it takes o coins to make 0 amount.

    Time Complexity: 
        The outer loop we iterate for amount times
        The inner loop we iterate for coin times 
        Overall: O (amount * coins)
    Space Complexity: 
        We store amount + 1 elements in the dp array but since we can ignore the 
        constant, the overall space complexity is O(amount)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      # initialize a dp array and fill it with amount + 1, we can also put any large value such as inf
      dp = [amount + 1] * (amount + 1)
      dp[0] = 0 # we know that it takes 0 coins to make 0 
      
      # since we already filled dp[0] with 0, we start our loop from index 1
      for i in range(1, amount + 1):
         # we loop through the coins list 
         for coin in coins:
            # we check the following line because if our i is 2 but the available coin in  1, we know 
            # that we can not make a 1 with a 2 values coin
            if i >= coin: 
               dp[i] = min(dp[i], dp[i - coin] + 1)
      return dp[amount] if dp[amount] != amount + 1 else -1

solution = Solution()
coins = [1,2,5]
amount = 3
print(solution.coinChange(coins, amount))
coins = [2]
amount = 3
print(solution.coinChange(coins, amount))
coins = [1]
amount = 0
print(solution.coinChange(coins, amount))
    
    