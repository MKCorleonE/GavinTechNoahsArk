"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""

# 我自己想的，但是超时了
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        while len(height) > 1:
            left = 0
            right = len(height) - 1
            while left < len(height) and height[left] == 0:
                left += 1
            while right >= 0 and height[right] == 0:
                right -= 1
            if left >= len(height) or right < 0 or left > right:
                break
            height = height[left:right + 1]
            ans += height.count(0)
            height = [x - 1 if x - 1 > 0 else 0 for x in height]
        return ans

# 最佳解答
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])  # 前缀最大值
            suf_max = max(suf_max, height[right])  # 后缀最大值
            if pre_max < suf_max:  # 可以确定 left 处的接水量
                ans += pre_max - height[left]
                left += 1  # 搞定了 left，现在问题缩小到 [left+1, right]
            else:  # 可以确定 right 处的接水量
                ans += suf_max - height[right]
                right -= 1  # 搞定了 right，现在问题缩小到 [left, right-1]
        return ans