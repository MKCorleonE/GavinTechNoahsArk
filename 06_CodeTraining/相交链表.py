"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交

题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

自定义评测：
评测系统 的输入如下（你设计的程序 不适用 此输入）：
"""

# 最佳答案，基于双指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB # 构建了两个指针A和B，分别指向两个链表的头节点
        while A != B:       # 当A和B不相等时，继续循环
            A = A.next if A else headB
            B = B.next if B else headA
        return A

# 笔记
# 时间复杂度：O(m+n)，其中 m 和 n 分别是两个链表的长度。最坏情况下，我们需要遍历两个链表各一次。
# 空间复杂度：O(1)。我们只使用了两个指针，并没有使用额外的空间来存储链表节点。
# 核心原理：两个指针把遍历完一个链表后，指向另一个链表的头节点，这样两个指针最终会在相交节点相遇，或者在都为 None 时结束循环。
# 关键是两个指针把总的遍历长度对齐了，这样就能保证在相交节点相遇。