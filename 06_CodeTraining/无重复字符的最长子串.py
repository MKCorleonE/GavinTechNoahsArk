"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

重点：
1. 子串必须是连续的
2. 子序列不要求连续
"""

# 最佳答案
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0   # 如果字符串为空，直接返回0
        left = 0 # 用来记录左边界
        lookup = set() # 用来存储当前子串中的字符
        n =len(s) 
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

# 复杂度分析：
# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。我们只需要遍历字符串一次。
# 空间复杂度：O(min(n, m))，其中 m 是字符集的大小。我们使用了一个集合来存储当前子串中的字符，最坏情况下需要 O(n) 的额外空间。