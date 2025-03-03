# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.index = -1
        self._inorder(root)
        
    def _inorder(self, root: Optional[TreeNode]):
        if not root:
            return None
        self._inorder(root.left)
        self.nodes.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()