"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。
多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。 

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2
"""

# 摩尔投票法
"""
记数组首个元素为 n1，众数为 x ，遍历并统计票数。
当发生票数和 = 0时，剩余数组的众数一定不变 ，这是由于：

当 n1 = x ： 抵消的所有数字中，有一半是众数 x 。
当 n1 != x ： 抵消的所有数字中，众数 x 的数量最少为 0 个，最多为一半。
利用此特性，每轮假设发生 票数和 = 0 都可以缩小剩余数组区间 。
当遍历完成时，最后一轮假设的数字即为众数。
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        x = 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        return x

# 哈希表
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)