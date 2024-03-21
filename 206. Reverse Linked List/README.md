# 206. Reverse Linked List

## Intuition
To reverse a linked list, we can iterate through the list and change the direction of each node's pointer. Initially, the `next` pointer of each node points to the next node in the original list. After reversing, the `next` pointer of each node should point to the previous node, effectively reversing the order of the list.

## Approach
We'll maintain two pointers, `last` and `curr`. `last` will initially be `None`, and `curr` will start at the head of the list. We'll iterate through the list, and for each node `curr`, we'll create a new node with the same value as `curr`, but with its `next` pointer pointing to `last`. Then, we'll update `last` to be the newly created node and move `curr` to the next node in the original list. By doing this, we effectively reverse the direction of the pointers.

## Complexity
- Time complexity: 
   - This approach traverses the entire linked list once, so the time complexity is O(n), where n is the number of nodes in the linked list.
- Space complexity: 
   - We're creating a new node for each node in the original list, so the space complexity is O(n) as well, where n is the number of nodes in the linked list.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last, curr = None, head
        while curr:
            dummy = ListNode(curr.val, last)
            last = dummy
            curr = curr.next

        return last
```