"""
给定一个整数数组 nums，按照顺序依次比较每两个相邻的元素，将比较结果转换为字符，并最终拼接为一个字符串返回。
比较规则：
- 如果前一个元素大于后一个元素，记录 >。
- 如果前一个元素小于后一个元素，记录 <。
- 如果两个元素相等，记录 =。
"""

# 最佳答案
def compare_adjacent(nums):
    result = []

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            result.append(">")
        elif nums[i] < nums[i + 1]:
            result.append("<")
        else:
            result.append("=")

    return "".join(result)


nums = [3, 5, 5, 2, 8]
print(compare_adjacent(nums))  # <=>工作

# 我的答案，双指针
def compare_adjacent(nums):
    ans = []
    p1 = 0
    p2 = 1
    for i in range(len(nums) - 1):
        if nums[p1] > nums[p2]:
            ans.append(">")
        elif nums[p1] < nums[p2]:
            ans.append("<")
        else:
            ans.append("=")
        p1 += 1
        p2 += 1
    return "".join(ans)   # 要求返回字符串，而不是列表，所以使用 "".join(ans) 将列表转换为字符串。

# 复杂度分析：
# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。我们只需要遍历数组一次。
# 空间复杂度：O(n)，用于存储比较结果的列表 ans。

# 原地修改，降低空间复杂度
def compare_adjacent(nums):
    n = len(nums)

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i] = ">"
        elif nums[i] < nums[i + 1]:
            nums[i] = "<"
        else:
            nums[i] = "="

    if nums:
        nums.pop()

    return nums