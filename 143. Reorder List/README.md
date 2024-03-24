# 143. Reorder List

## Intuition
To reorder a singly-linked list, the approach involves splitting the list into two halves, reversing the second half, and then merging the two halves alternatively.

## Approach
1. **Splitting the List**: Use the slow and fast pointer technique to find the middle of the list. 
2. **Reversing the Second Half**: Reverse the second half of the list starting from the node after the middle node.
3. **Merging Two Halves**: Merge the first half and the reversed second half alternately.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1).

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        """
        Reverses a linked list.
        """
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
        """
        Merges two linked lists.
        """
        while right:
            nextNode = left.next
            left.next = right
            left = right
            right = nextNode

    def reorderList(self, head):
        """
        Reorders a linked list in-place.
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
```
