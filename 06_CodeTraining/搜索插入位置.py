"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
"""

# 最佳答案，二分查找法
def search_insert(nums, target):
    left, right = 0, len(nums) - 1   # 初始化左右指针，left 指向数组的起始位置，right 指向数组的末尾位置（双指针）

    while left <= right:   # 当左指针小于等于右指针时，继续循环
        mid = (left + right) // 2   # 计算中间位置的索引 mid，使用整除运算符 //，确保 mid 是整数（返回商的整数部分）

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# 复杂度分析：
# 时间复杂度：O(log n)，其中 n 是数组 nums 的长度。我们使用二分查找算法，每次将搜索范围减半，因此时间复杂度为 O(log n)。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储变量 left、right 和 mid，因此空间复杂度为 O(1)。

# 笔记：
# //运算符表示整除运算，即返回商的整数部分。例如，5 // 2 的结果是 2，而不是 2.5。

