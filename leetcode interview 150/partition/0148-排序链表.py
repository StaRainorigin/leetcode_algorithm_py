# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 边界条件
        if not head:
            return None
        if not head.next:
            return head
        
        # 快慢指针找到中间节点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # 断开链表
        pre = slow
        slow = slow.next
        pre.next = None
        
        # 递归排序, 分别对左右两个链表排序
        node1 = self.sortList(head)
        node2 = self.sortList(slow)
        
        # 合并链表
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
        # 处理剩余节点
        if node1:
            cur.next = node1
        if node2:
            cur.next = node2
        
        # 返回排序后的链表
        return dummy.next
        
    
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
        
    #     nodes: List[ListNode] = []
    #     node = head
    #     while node:
    #         nodes.append(node)
    #         node = node.next
            
    #     nodes = sorted(nodes, key=lambda node: node.val)
        
    #     for i in range(0, len(nodes)-1):
    #         nodes[i].next = nodes[i+1]
    #     nodes[-1].next = None
        
    #     return nodes[0]
    
if __name__ == "__main__":
    dummy = ListNode()
    cur = dummy
    nums = [4, 2, 1, 3]
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    node = Solution().sortList(dummy.next)
    while node:
        print(node.val, end=' ')
        node = node.next
    