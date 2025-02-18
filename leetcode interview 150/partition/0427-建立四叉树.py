"""
# Definition for a QuadTree node.
"""
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        
        def is_leaf(grid: List[List[int]]) -> bool:
            return all(all(cell == grid[0][0] for cell in row) for row in grid)
        
        n = len(grid)
        if is_leaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        else:
            mid = n // 2
            topLeft = [gird[:mid] for gird in grid[:mid]]
            topRight = [gird[mid:] for gird in grid[:mid]]
            bottomLeft = [gird[:mid] for gird in grid[mid:]]
            bottomRight = [gird[mid:] for gird in grid[mid:]]
            return Node(0, False, self.construct(topLeft), self.construct(topRight), self.construct(bottomLeft), self.construct(bottomRight))
        