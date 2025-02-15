# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans: List[float] = []
        nodes: List[int] = []
        
        def dfs (node: Optional[TreeNode], depth: int):
            if node is None:
                return
            if len(ans) == depth:
                ans.append(float(node.val))
                nodes.append(1)
            else:
                temp = ans[depth] * nodes[depth]
                nodes[depth] += 1
                ans[depth] = (temp + node.val)/nodes[depth]
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            
        dfs(root, 0)
        return ans
    
    
    
    def averageOfLevels1(self, root: Optional[TreeNode]) -> List[float]:
        pass