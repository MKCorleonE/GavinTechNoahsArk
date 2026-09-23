"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""

# 最佳答案，使用滑动窗口
from collections import Counter

def findAnagrams(s: str, p: str):
    if len(s) < len(p):    # 如果 s 的长度小于 p 的长度，直接返回空列表
        return []
    
    need = Counter(p)      # 目标窗口
    window = Counter()     # 当前窗口
    left = 0
    res = []
    
    for right, ch in enumerate(s):
        # 右边界字符加入窗口
        window[ch] += 1
        
        # 窗口长度超过 p 的长度，左边界收缩
        if right - left + 1 > len(p):
            left_ch = s[left]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            left += 1
        
        # 窗口长度正好等于 p 的长度时，判断是否为异位词
        if right - left + 1 == len(p):
            if window == need:
                res.append(left)
    
    return res


# 笔记
# 异位词（Anagram）的定义是：
# 两个字符串包含的字符种类和每个字符出现的次数完全相同，只是顺序可以不同。
# 注意关键词是 “可以不同”，而不是 “必须不同”。

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。
# 空间复杂度：O(1)，因为字符集的大小是固定的（26个字母）。

# 滑动窗口
# 使用滑动窗口的方法来解决这个问题。我们维护一个窗口，窗口的大小等于字符串 p 的长度。
# 在每次移动窗口时，我们更新窗口内的字符计数，并与字符串 p 的字符计数进行比较。
# 如果两者相等，则说明当前窗口内的子串是字符串 p 的异位词。

# enumerate()函数：第一个是索引，第二个是值

# 另外一种写法：
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        res = []
        if s_count == p_count:
            res.append(0)
        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_count == p_count:
                res.append(i - len(p) + 1)
        return res