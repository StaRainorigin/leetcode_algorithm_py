# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        
        def inorder(node: Optional[TreeNode]):
            if not node: return
            nonlocal count, ans, k
            inorder(node.left)
            count += 1
            if count is k:
                ans = node.val
            elif count > k:
                return
            inorder(node.right)
        
        inorder(root)
        return ans