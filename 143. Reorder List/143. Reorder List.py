class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        if not head:
            return None

        prev, curr = None, head
        nextNode = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def merge(self, left, right):
        while right:
            nextNode = left.next
            left.next = right
            left = right
            right = nextNode

    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        prev.next = None
        left = head
        right = self.reverse(slow)
        self.merge(left, right)



        