"""
给定一个二叉树的根节点 root ，返回它的前序遍历。

前序遍历的顺序是：根节点 -> 左子树 -> 右子树。

示例1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例2：
输入：root = []
输出：[]
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1  # 白色表示未访问，灰色表示准备访问节点本身
        res = []
        stack = [(WHITE, root)]

        while stack:
            color, node = stack.pop()
            if node is None:
                continue

            if color == WHITE:
                # 栈是先进后出，因此按右、左、根入栈，出栈顺序就是根、左、右。
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)

        return res


# 笔记
# 前序遍历的核心是“根节点最先访问”：根 -> 左 -> 右。
# 使用颜色标记时：
# 1. 白色节点表示第一次遇到，需要展开它的子树。
# 2. 灰色节点表示子树已经安排好，下一次弹出时访问节点本身。
# 3. 因为栈先进后出，所以入栈顺序要反过来：右、左、根。
#
# 时间复杂度：O(n)，每个节点最多入栈、出栈各两次。
# 空间复杂度：O(n)，最坏情况下栈中可能保存整棵树。