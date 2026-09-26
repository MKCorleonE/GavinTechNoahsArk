"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""

# 我的答案，部分用例无法通过
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        ans = False
        target_len = len(nums) - 1
        max_len = 1
        for i in range(target_len):
            max_len = nums[i]
            if max_len >= target_len:
                ans = True
            target_len -= 1
        return ans


# 最佳答案，贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是数组的长度。
# 空间复杂度：O(1)，只使用了常数级别的额外空间。

# 另外一个最佳答案
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i