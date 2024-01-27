# 876. Middle of the Linked List

## Intuition
The problem asks for finding the middle node of a linked list. One simple approach is to first calculate the length of the linked list and then traverse it again to find the middle node.

## Approach
1. Initialize a variable `length` to 0 to keep track of the length of the linked list.
2. Traverse the linked list while updating the length.
3. Once the length is determined, iterate through the linked list again until the middle node is reached.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the linked list. The first loop to calculate the length takes O(n) time, and the second loop to find the middle node also takes O(n/2) time in the worst case, but we simplify it to O(n).
- Space complexity: O(1), as we only use a constant amount of extra space for variables `length` and `curr`.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        
        # Calculate the length of the linked list
        while curr is not None:
            curr = curr.next
            length += 1
        
        # Traverse to the middle node
        for i in range(int(length/2)):
            head = head.next
        
        return head
