# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: 
            return None
        mid = len(nums) // 2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))
    
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
    #     def build(left: int, right: int) -> Optional[TreeNode]:
    #         if left > right:
    #             return None
    #         mid = (left + right) // 2
    #         return TreeNode(nums[mid], build(left, mid-1), build(mid+1, right))
        
    #     return build(0, len(nums)-1)
            
            
            