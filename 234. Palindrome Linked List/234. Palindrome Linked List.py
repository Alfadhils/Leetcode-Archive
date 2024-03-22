from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head):
            last, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = last
                last = curr
                curr = next_node
            return last
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = reverseList(slow)

        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next

        return True
        