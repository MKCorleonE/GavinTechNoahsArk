"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
"""

# 最佳答案，动态规划，定义状态：dp[i] 表示以 nums[i] 结尾的最大子数组和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)   # 获取数组 nums 的长度
        if size == 0:
            return 0       # 如果数组为空，返回 0（特殊情况退出）
        dp = [0 for _ in range(size)]   # 初始化 dp 数组，长度为 size，初始值为 0

        dp[0] = nums[0]   # 边界：以第一个元素结尾的最大和就是它自己
        for i in range(1, size):   # 遍历数组 nums，从第二个元素开始。要么自己单独开头，要么接在前面的最优解后面。
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]   # 前面的和 >= 0，接上它只会更大（或不变）
            else:
                dp[i] = nums[i]   # 前面的和 < 0，接上它反而变小，不如从自己重新开始
        return max(dp)   # 答案是所有 dp[i] 中的最大值

# 复杂度分析：
# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。我们只需要遍历一次数组。
# 空间复杂度：O(n)，我们使用了一个额外的数组 dp 来存储每个位置的最大子数组和。

# 笔记：
# 动态规划的核心思想是将问题分解为子问题，并利用子问题的解来构建原问题的解。
# 为了保证计算子问题能够按照顺序、不重复地进行，动态规划要求已经求解的子问题不受后续阶段的影响。
# 这个条件也被叫做「无后效性」。换言之，动态规划对状态空间的遍历构成一张有向无环图，遍历就是该有向无环图的一个拓扑序。
# 有向无环图中的节点对应问题中的「状态」，图中的边则对应状态之间的「转移」，转移的选取就是动态规划中的「决策」。

# 降低空间复杂度的优化：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            ans = max(ans, current)

        return ans