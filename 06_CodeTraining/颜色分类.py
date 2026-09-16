"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，
原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
"""

# 我的答案 (违反了不允许创建独立的Θ(n)-大小容器的限制)
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_0 = 0
        num_1 = 0
        num_2 = 0
        for num in nums:
            if num == 0:
                num_0 += 1
            if num == 1:
                num_1 += 1
            if num == 2:
                num_2 += 1
        nums = [0] * num_0 + [1] * num_1 + [2] * num_2

# 最佳答案 (双指针)
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1