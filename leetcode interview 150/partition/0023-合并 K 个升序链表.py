# Definition for singly-linked list.

from typing import List, Optional
from heapq import heappush, heappop, heapify

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda x, y: x.val < y.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def merge (node1: Optional[ListNode], node2: Optional[ListNode]):
            dummy = ListNode()
            cur = dummy
            while node1 and node2:
                if node1.val < node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next
            
            cur.next = node1 if node1 else node2
            return dummy.next
        
        # dummy = ListNode()
        # cur = dummy
        # for node in lists:
        #     cur.next = merge(cur.next, node)
        
        # return dummy.next
        
        left = self.mergeKLists(lists[:len(lists) // 2])
        right = self.mergeKLists(lists[len(lists) // 2:])
        return merge(left, right)
        
    
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
        
    #     heads = [node for node in lists if node]
        
    #     heapify(heads)
    #     dummy = ListNode()
    #     cur = dummy
        
    #     while heads:
    #         node = heappop(heads)
    #         if node.next:
    #             heappush(heads, node.next)
    #         cur.next = node
    #         cur = cur.next
        
    #     return dummy.next
        
        
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
        
    #     nodes = []
    #     for node in lists:
    #         while node:
    #             nodes.append(node)
    #             node = node.next
        
    #     nodes.sort(key=lambda x: x.val)
        
    #     dummy = ListNode()
    #     cur = dummy
    #     for node in nodes:
    #         cur.next = node
    #         cur = cur.next
        
    #     return dummy.next
        