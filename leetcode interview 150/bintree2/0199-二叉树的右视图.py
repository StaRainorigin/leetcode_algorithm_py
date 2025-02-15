# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes: List[int] = []
        
        def dfs(node: Optional[TreeNode], depth: int):
            if node is None:
                return
            if len(nodes) == depth:
                nodes.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
                
        dfs(root, 0)
        return nodes