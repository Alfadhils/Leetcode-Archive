from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last, curr = None, head
        while curr:
            dummy = ListNode(curr.val, last)
            last = dummy
            curr = curr.next

        return last
        