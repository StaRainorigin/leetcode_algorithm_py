# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        ans: List[List[int]] = []
        queue: List[TreeNode] = []
        queue.append(root)
        
        while len(queue) != 0:
            vals, nodes = [], []
            for node in queue:
                vals.append(node.val)
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
            ans.append(vals)
            queue = nodes
            
        return ans
            

            