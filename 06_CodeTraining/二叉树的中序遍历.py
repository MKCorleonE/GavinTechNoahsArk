"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例2：
输入：root = []
输出：[]
"""

# 最佳答案
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1   # 白色表示未访问过，灰色表示访问过
        res = []
        stack = [(WHITE, root)]     # Leedcode会处理数组输入，这里的root是一个TreeNode对象
        while stack:
            color, node = stack.pop()  # 取出栈顶元素，栈顶相当于数组的最后一个元素
            if node is None: continue
            if color == WHITE: 
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

# 笔记
# 二叉树的三种深度优先遍历
# 二叉树每个节点最多有两个子节点：左孩子、右孩子。根据“根节点”被访问的时机，分为三种：
#          根
#         /  \
#        左   右
# 1. 前序遍历（根-左-右）
# 2. 中序遍历（左-根-右）
# 3. 后序遍历（左-右-根）
# 栈是一种 先进后出 的结构，出栈顺序为 左，中，右
# 那么入栈顺序必须调整为倒序，也就是 右，中，左
# 同理，如果是前序遍历，入栈顺序为 右，左，中；后序遍历，入栈顺序中，右，左

# 关于“栈”
# 栈是一种先进后出的数据结构，栈的操作主要有两种：入栈（push）和出栈（pop）。
# Python 里通常就用 list 来当栈用，因为：
# 1. list.append() 方法可以在列表末尾添加一个元素，相当于入栈操作。
# 2. list.pop() 方法可以移除列表末尾的一个元素，并返回该元素，相当于出栈操作。
# 只要只在末尾加、只在末尾取，list 的行为就是栈。