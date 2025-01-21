class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


solution = Solution()

# Example 1
amount = 5
coins = [1, 2, 5]
print("Input: amount =", amount, ", coins =", coins)
print("Output:", solution.change(amount, coins))  

# Example 2
amount = 3
coins = [2]
print("\nInput: amount =", amount, ", coins =", coins)
print("Output:", solution.change(amount, coins))  

# Example 3
amount = 10
coins = [10]
print("\nInput: amount =", amount, ", coins =", coins)
print("Output:", solution.change(amount, coins)) 
