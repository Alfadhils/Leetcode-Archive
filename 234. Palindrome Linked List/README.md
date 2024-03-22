# 234. Palindrome Linked List

## Intuition
To determine if a linked list is a palindrome, we can reverse the second half of the list and then compare it with the first half. This approach utilizes the concept of fast and slow pointers to find the midpoint of the list efficiently.

## Approach
1. Define a function `reverseList` to reverse a linked list.
2. Initialize two pointers `slow` and `fast` to the head of the list.
3. Move `slow` by one step and `fast` by two steps until `fast` reaches the end of the list or `fast.next` reaches the end of the list.
4. Reverse the second half of the list starting from `slow`.
5. Traverse both the original first half and the reversed second half simultaneously and compare the values of corresponding nodes.
6. If at any point the values don't match, return False. Otherwise, return True.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the linked list. We traverse the entire list once to find the midpoint and once again to compare values.
- Space complexity: O(1), since we are using a constant amount of extra space.

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```