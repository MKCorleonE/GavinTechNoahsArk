"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
"""

# 最佳答案，哈希表
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # 将字符串排序后作为键
            key = ''.join(sorted(s))   # sorted() 函数会将字符串中的字符按字母顺序排序，返回一个列表，然后使用 ''.join() 将其连接成一个新的字符串。
            if key not in anagrams:    # 这里查的是键是否存在，而不是值是否存在
                anagrams[key] = []     # 如果键不存在，则创建一个新的列表作为值
            anagrams[key].append(s)    # 将原始字符串添加到对应的键的值
        return list(anagrams.values()) # 由于 anagrams 是一个字典，我们只需要返回它的值（即所有的异位词组），所以使用 list(anagrams.values()) 将其转换为列表。

# 复杂度分析：
# 时间复杂度：O(n * k log k)，其中 n 是字符串数组 strs 的长度，k 是 strs 中字符串的最大长度。
# 对于每个字符串，我们需要对其进行排序，排序的时间复杂度是 O(k log k)。
# 空间复杂度：O(n * k)，用于存储哈希表中的所有异位词组。