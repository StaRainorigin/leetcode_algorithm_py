# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        pre: TreeNode = None
        def inorder(node: Optional[TreeNode]):
            if not node: return
            nonlocal ans, pre
            
            inorder(node.left)
            if pre:
                ans = min(ans, abs(node.val - pre.val))
            pre = node
            inorder(node.right)
            
        inorder(root)
        return ans