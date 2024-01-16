# 2. Add Two Numbers

## Intuition

The problem involves adding two numbers represented as linked lists. My initial intuition is to simulate the process of adding numbers, keeping track of the carry, and constructing a new linked list to store the result.

## Approach

The approach is to iterate through the linked lists simultaneously, adding corresponding digits along with any carry from the previous step. We use a dummy node to simplify the code and keep track of the current node in the result linked list. The carry is updated for each step, and the result is stored in a new linked list.

## Complexity

- Time complexity:

The time complexity of this solution is O(max(m, n)), where m and n are the lengths of the input linked lists. We iterate through both linked lists once.

- Space complexity:

The space complexity is O(max(m, n)), where m and n are the lengths of the input linked lists. This is because we create a new linked list to store the result, and the length of the result can be at most max(m, n) + 1.

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
  
            curr = curr.next 

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next 
```
