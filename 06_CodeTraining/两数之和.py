"""
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
"""

# 最佳答案 使用哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}  # 创建一个空哈希表（字典）
        for j, x in enumerate(nums):  # x=nums[j]
            if target - x in idx:  # 在左边找 nums[i]，满足 nums[i]+x=target
                return [idx[target - x], j]  # 返回两个数的下标
            idx[x] = j  # 保存 nums[j] 和 j

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。我们只遍历了数组一次，每次查找哈希表的时间复杂度为 O(1)。
# 空间复杂度：O(n)，其中 n 是数组 nums 的长度。最坏情况下，我们需要将数组中的所有元素存储在哈希表中。

# 笔记
# x in idx 是在哈希表中查找key的操作，时间复杂度为 O(1)。
# x in idx.values() 是在哈希表中查找value的操作，时间复杂度为 O(n)。
# dict[x] 是获取哈希表中key对应的value，时间复杂度为 O(1)。