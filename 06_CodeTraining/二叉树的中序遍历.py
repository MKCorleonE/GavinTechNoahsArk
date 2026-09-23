"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。


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
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
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
# 1. 前序遍历（根-左-右）
# 2. 中序遍历（左-根-右）
# 3. 后序遍历（左-右-根）