"""
题目：第一个只出现一次的字符
给定一个长度为 n 的字符串，字符串只由字母组成。
请从中找到第一个只出现一次的字符，并返回它的位置；
如果不存在这样的字符，则返回 -1。
字母需要区分大小写，字符的位置从 0 开始计数。

数据范围：
0 <= n <= 10000
"""

from collections import Counter # 哈希表涉及的包


def first_unique_position(s: str) -> int:
    # 用哈希表统计每个字符的出现次数
    count = Counter(s)                        # 从高到低排序的

    # 从左到右寻找第一个出现次数为 1 的字符
    for index, ch in enumerate(s):
        if count[ch] == 1:
            return index

    # 没有只出现一次的字符
    return -1


# 测试示例
if __name__ == "__main__":
    print(first_unique_position("aAbac"))  # 1，字符 'A'
    print(first_unique_position("aabbcc"))  # -1