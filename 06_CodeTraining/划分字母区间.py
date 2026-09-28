"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 

示例 2：
输入：s = "eccbbbbdec"
输出：[10]
"""

# 最佳答案，贪心算法
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}  # 每个字母最后出现的下标，使用字典存储
        ans = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])  # 更新当前区间右端点的最大值
            if end == i:  # 当前区间合并完毕
                ans.append(end - start + 1)  # 区间长度加入答案
                start = end + 1  # 下一个区间的左端点
        return ans

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。
# 空间复杂度：O(1)，因为字符集的大小是固定的（最多 26 个字母）。

# 笔记
# 1. 使用贪心算法，每次尽可能多地划分一个区间。
# 2. 通过记录每个字符最后出现的位置，可以确定每个区间的右端点。
# 3. 当一个区间的右端点达到当前字符的位置时，说明该区间可以被划分。

# 把last = {c: i for i, c in enumerate(s)}展开写是：
# last = {}
# for i, c in enumerate(s):
#     last[c] = i

# enumerate(s) 返回的是一个包含索引和值的元组的迭代器，所以 i 是索引，c 是值。

# 集合是什么符号
# 集合的符号是 {}，例如：{1, 2, 3}。

# 字典是什么符号
# 字典的符号是 {}，例如：{"a": 1, "b": 2}。

# 那last = {}，既可表示一个空字典，也可表示一个空集合，这句话是对的吗？
# 这句话是不对的。在 Python 中，{} 表示一个空字典，而不是空集合。空集合应该用 set() 来表示。