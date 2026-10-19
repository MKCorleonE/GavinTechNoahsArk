"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
测试用例保证输出的长度不会超过 105。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""

# 最佳答案，辅助栈法
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0   # 重置 res 和 multi，以便处理括号内的字符串和数字
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':   # 判断字符 c 是否为数字字符，但此时的 c 是字符串类型，所以需要将其转换为整数类型
                multi = multi * 10 + int(c)   # 处理多位数的情况，例如 12[ab]，需要将 multi 乘以 10 再加上当前数字
            else:  
                res += c
        return res

# 复杂度分析：
# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。每个字符都被遍历一次，且每个字符最多被压入和弹出栈一次。
# 空间复杂度：O(n)，栈的空间取决于嵌套的深度，最坏情况下，栈的大小为 n/2。

# 笔记：
# 本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。
# 栈的类型都是 list，栈中存储的是一个列表，列表中包含两个元素：当前的 multi 和 res。
# {}是字典，[]是列表，()是元组。 
# elif '0' <= c <= '9': 判断字符 c 是否为数字字符，但此时的 c 是字符串类型，所以需要将其转换为整数类型
