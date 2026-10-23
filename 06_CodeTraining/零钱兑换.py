"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount，表示总金额。
计算并返回可以凑成总金额所需的 最少 的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
"""

# 最佳答案，动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 第一步：初始化 dp 数组
        dp = [float('inf')] * (amount + 1)   # 初始化
        dp[0] = 0                            # 初始状态

        # 第二步：计算从 1 到 amount 的所有状态
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # 第三步：返回答案
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

# 解题步骤：
# 定义子问题：子问题就是 “凑成金额 k 所需的最少硬币个数 ”，用 f(k) 表示。
# 写出子问题的递推关系以及初始条件：
# f(k) = min{ f(k-coin) + 1 }，其中 coin 是所有硬币的面额。
# 初始条件：
# f(0) = 0，因为凑成金额 0 不需要任何硬币。