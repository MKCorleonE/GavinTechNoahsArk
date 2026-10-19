"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
"""

# 最佳答案，单调栈，从右向左遍历
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n   # 初始化答案
        st = []   # 初始化栈
        for i in range(n - 1, -1, -1):  # 从右向左遍历 temperatures 数组，且包含第一个元素
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i   # 计算下一个更高温度出现的天数，st[-1] 是栈顶元素的索引，i 是当前元素的索引，两者相减得到天数
            st.append(i)   # 压入的是索引，而不是温度值，这样可以方便计算天数
        return ans

# 复杂度分析：
# 时间复杂度：O(n)，其中 n 是数组 temperatures 的长度。每个元素最多被压入和弹出栈一次。
# 空间复杂度：O(min(n,U))，其中 U=max(temperatures)−min(temperatures)+1，栈的空间取决于温度的范围，最坏情况下，栈的大小为 n。

# 最佳答案，单调栈，从左向右遍历
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []  # todolist
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:   # 这里是while循环，因为可能有多个元素需要出栈，直到栈顶元素大于当前温度 t
                j = st.pop()  # 返回栈顶元素的索引
                ans[j] = i - j
            st.append(i)
        return ans

# 复杂度分析：
# 时间复杂度：O(n)，其中 n 是数组 temperatures 的长度。每个元素最多被压入和弹出栈一次。
# 空间复杂度：O(n)。注意这种写法栈中可以有重复元素。

# 笔记：
# range(n - 1, -1, -1) 表示从 n-1 到 0（包含 0），步长为 -1，即从右向左遍历。
# 如果是range(n-1, 0, -1)，则表示从 n-1 到 1（不包含 0），步长为 -1，即从右向左遍历，但不包括第一个元素。
# for i, t in enumerate(temperatures): 其中i是索引，t是对应的温度值。
# enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标。
# 索引在前，值在后，返回的是一个 enumerate 对象，可以使用 list() 转换为列表。
# append() 方法用于在列表末尾添加新的元素。