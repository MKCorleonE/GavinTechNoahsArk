"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

示例 1 ：
输入：nums = [2,2,1]
输出：1

示例 2 ：
输入：nums = [4,1,2,1,2]
输出：4

示例 3 ：
输入：nums = [1]
输出：1
"""

# 最佳答案
from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)      
        # reduce()函数是将序列中的元素依次两两合并进行操作。

"""
异或运算的性质：
a ^ a == 0      # 相同数字异或会抵消
a ^ 0 == a      # 与 0 异或不变
a ^ b == b ^ a  # 顺序无关

所以：
2 ^ 3 ^ 2
= (2 ^ 2) ^ 3
= 0 ^ 3
= 3
"""