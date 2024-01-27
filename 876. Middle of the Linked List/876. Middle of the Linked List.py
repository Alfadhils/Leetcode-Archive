from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        
        for i in range(int(length/2)):
            head = head.next
        return head