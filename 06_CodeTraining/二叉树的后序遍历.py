"""
给定一个二叉树的根节点 root ，返回它的后序遍历。

后序遍历的顺序是：左子树 -> 右子树 -> 根节点。

示例1：
输入：root = [1,null,2,3]
输出：[3,2,1]

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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1  # 白色表示未访问，灰色表示准备访问节点本身
        res = []
        stack = [(WHITE, root)]

        while stack:
            color, node = stack.pop()
            if node is None:
                continue

            if color == WHITE:
                # 栈是先进后出，因此按根、右、左入栈，出栈顺序就是左、右、根。
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)

        return res


# 笔记
# 后序遍历的核心是“根节点最后访问”：左 -> 右 -> 根。
# 使用颜色标记时，灰色节点必须等左右子树都处理完后再出栈访问。
# 因为栈先进后出，所以入栈顺序要反过来：根、右、左。
#
# 时间复杂度：O(n)，每个节点最多入栈、出栈各两次。
# 空间复杂度：O(n)，最坏情况下栈中可能保存整棵树。