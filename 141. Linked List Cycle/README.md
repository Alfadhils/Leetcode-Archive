# 141. Linked List Cycle

## Intuition
The problem asks us to detect a cycle in a linked list. A linked list is said to have a cycle if the tail node references another existing node in the list. We can use the two-pointer approach, also known as the "hare and tortoise algorithm," to solve the problem.

## Approach
The two-pointer method we use has the `slow` and `fast` pointers. The solution utilizes a `fast` pointer that traverses the list twice as fast as the `slow` pointer. If there's no cycle, the `fast` pointer will reach the end and break the loop. However, if there's a cycle, eventually the `fast` and `slow` pointers will point to the same node. In this case, we conclude that the linked list has a cycle.

## Complexity
- Time complexity: O(n). The tortoise and hare algorithm is known to have O(n) complexity.
- Space complexity: O(1). The algorithm uses a constant amount of space.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False 
```