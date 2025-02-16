"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        maps = {}
        
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in maps: return maps[node]
            
            clone_node = Node(node.val)
            maps[node] = clone_node
            
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
                
            return clone_node
    
        return dfs(node)