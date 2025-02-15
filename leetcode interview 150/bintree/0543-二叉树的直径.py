# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            nonlocal ans
            ans = max(ans, left + right)
            return max(left, right)
        dfs(root)
        return ans
            