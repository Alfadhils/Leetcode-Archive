from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cumsum = 0
        last_idx = {}
        dummy = ListNode(0)
        dummy.next = head
        last_idx[0] = dummy
        while head:
            cumsum += head.val
            if cumsum in last_idx:
                last = last_idx[cumsum]
                temp = last
                csum = cumsum
                while temp != head:
                    temp = temp.next
                    csum += temp.val
                    if temp != head:
                        del last_idx[csum]
                last.next = head.next
            else:
                last_idx[cumsum] = head
            head = head.next
        return dummy.next
        