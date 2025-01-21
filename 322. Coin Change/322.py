class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0

        for coin in coins:

            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != max_value else -1

solution = Solution()

# Example 1
coins = [1, 2, 5]
amount = 11
print("Input: coins =", coins, ", amount =", amount)
print("Output:", solution.coinChange(coins, amount)) 

# Example 2
coins = [2]
amount = 3
print("\nInput: coins =", coins, ", amount =", amount)
print("Output:", solution.coinChange(coins, amount))

# Example 3
coins = [1]
amount = 0
print("\nInput: coins =", coins, ", amount =", amount)
print("Output:", solution.coinChange(coins, amount)) 
