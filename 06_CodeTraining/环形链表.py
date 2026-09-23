"""
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
"""

# 最佳答案，使用哈希表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()             # 创建一个空集合来存储已经访问过的节点
        while head:
            if head in seen:
                return True
            seen.add(head)       # 将当前节点添加到集合中，对于集合来说 .add() 方法是用来添加一个元素，时间复杂度是 O(1)，不会添加重复的元素。
            head = head.next
        return False

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是链表中的节点数。每个节点最多被访问一次。
# 空间复杂度：O(n)，其中 n 是链表中的节点数。最坏情况下，链表中没有环，所有节点都被存储在集合中。

# 最佳答案，使用快慢指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:   # 如果链表为空或者只有一个节点，则不可能有环
            return False
        
        slow = head        # 慢指针在后
        fast = head.next   # 快指针在前
        
        while slow != fast:   # 当慢指针和快指针不相遇时，继续循环
            if not fast or not fast.next:   # 如果快指针到达链表末尾，则说明没有环
                return False
            slow = slow.next
            fast = fast.next.next  # 快指针每次移动两步，如果有环，快指针最终会追上慢指针（套圈）
            
        return True

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是链表中的节点数。每个节点最多被访问一次。
# 空间复杂度：O(1)，只使用了两个指针。