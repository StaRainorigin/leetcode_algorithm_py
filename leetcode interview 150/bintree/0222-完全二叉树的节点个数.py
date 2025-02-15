# Definition for a binary tree node.
from typing import Optional

# """
# 完全二叉树的性质可以让我们更高效地计算节点个数：
# 如果左子树的高度等于右子树的高度，则左子树是满二叉树，节点数为 2^h - 1，加上根节点，然后递归计算右子树。
# 如果左子树的高度大于右子树的高度，则右子树是满二叉树，节点数为 2^h - 1，加上根节点，然后递归计算左子树。
# """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = 0
        node = root
        while node:
            left_height += 1
            node = node.left
            
        right_height = 0
        node = root
        while node:
            right_height += 1
            node = node.right
            
        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            self.countNodes(root.left) + self.countNodes(root.right) + 1