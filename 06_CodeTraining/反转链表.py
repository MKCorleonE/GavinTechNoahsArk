"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""

# 最佳答案
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre   # 要在更新pre之前，先把cur.next指向pre，否则会丢失后续节点
            pre = cur        # 从这一步开始，pre不再是None，而是指向当前节点cur，并且是一个LinkedList类了。
            cur = tmp
        return pre

# 笔记
# 时间复杂度：O(n)，其中 n 是链表的长度。我们需要遍历整个链表一次。
# 空间复杂度：O(1)。我们只使用了常数级别的额外空间来存储指针变量。

# 递归法，思考难度高，不推荐
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回
