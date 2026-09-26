"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

示例 2:
输入: numRows = 1
输出: [[1]]
"""

# 最佳答案，动态规划
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = []
        for i in range(numRows):
            c.append([1] * (i + 1))
        for i in range(2, numRows):
            for j in range(1, i):
                # 左上方的数 + 正上方的数
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
        return c

# 复杂度分析
# 时间复杂度：O(numRows^2)，其中 numRows 是杨辉三角的行数。因为我们需要生成 numRows 行，每行最多有 numRows 个元素。
# 空间复杂度：O(1)，只使用了常数级别的额外空间，返回值不计入。


# 笔记
# 把杨辉三角的每一排左对齐：
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
# 每一排的第一个数和最后一个数都是 1，即 c[i][0]=c[i][i]=1。
# 其他数 c[i][j] = c[i-1][j-1] + c[i-1][j]，即左上方的数 + 正上方的数。