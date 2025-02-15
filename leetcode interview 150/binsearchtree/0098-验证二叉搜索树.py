# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre: int = -inf
        ans: bool = True
        
        def dfs(node: Optional[TreeNode]):
            nonlocal ans
            if not node or not ans: return
            nonlocal pre
            dfs(node.left)
            if pre and not pre < node.val:
                ans = False
                return
            pre = node.val
            dfs(node.right)
        
        dfs(root)
        return ans
                