"""
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
你必须编写一个时间复杂度为 O(log(m * n)) 的解决方案。

示例1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
"""

# 最佳答案，二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])   # 获取矩阵的行数和列数
        left, right = 0, m * n - 1           # 将矩阵视为一维数组，左边界为0，右边界为m*n-1，双指针
        while left + 1 < right:              # 当左指针和右指针之间的距离大于1时，继续循环
            mid = (left + right) // 2        # 二分查找，计算中间位置
            x = matrix[mid // n][mid % n]    # 将一维数组的索引转换为二维矩阵的行列索引，获取中间位置的元素
                                             # mid // n 表示行索引，mid % n 表示列索引
            if x == target:
                return True
            if x < target:
                left = mid + 1                   
            else:
                right = mid - 1                
        return False

# 复杂度分析：
# 时间复杂度：O(log(m * n))，其中 m 和 n 分别是矩阵的行数和列数。我们使用二分查找算法在矩阵中查找目标值。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间。

# 笔记：
# 二分查照一般搭配双指针使用，左指针和右指针分别指向数组的两端，然后不断缩小搜索范围，直到找到目标值或者搜索范围为空。
# //是整除运算符，表示取整除的结果，即整数部分。
# % 是取模运算符，表示取余数的结果。