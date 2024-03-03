# 19. Remove Nth Node From End of List

## Intuition
The problem requires removing the nth node from the end of a singly linked list. A straightforward solution involves iterating through the list to calculate its length, then finding the node index to remove. However, we aim to achieve this within a single pass, which can be accomplished using a two-pointer approach known as the slow-fast pointer method.

## Approach
The slow-fast pointer method involves using two pointers: a fast pointer to traverse through the list quickly and a slow pointer to find specific nodes. By adjusting the positions of these pointers, we can efficiently determine the node to remove with just one pass through the list.

## Complexity
- Time complexity: O(N), where N is the number of nodes in the linked list.
- Space complexity: O(1), as we use a constant amount of extra space for the pointers.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next is not None else None

        return dummy.next
```
