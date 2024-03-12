# 1171. Remove Zero Sum Consecutive Nodes from Linked List

## Intuition
The problem requires repeatedly removing consecutive sequences of nodes from the linked list that sum to zero. To efficiently do this, we can utilize a hashmap to keep track of cumulative sums encountered so far along with their corresponding node positions. As we traverse the linked list, whenever we encounter a cumulative sum that we've seen before, it implies that the sequence between the current node and the node where this sum was previously encountered sums to zero. Hence, we can remove that sequence.

## Approach
1. Initialize a cumulative sum variable (`cumsum`) to keep track of the running sum as we traverse the linked list.
2. Use a hashmap (`last_idx`) to store the last occurrence of each cumulative sum along with its corresponding node position.
3. Initialize a dummy node to simplify handling the edge case where the entire list sums to zero.
4. Traverse the linked list while updating the cumulative sum.
5. If the current cumulative sum is already in the hashmap, it means there exists a subsequence with a sum of zero.
   - Retrieve the last node where this cumulative sum occurred (`last`) and update its next pointer to skip the subsequence.
   - Also, remove all entries from the hashmap between the last node and the current node.
6. If the current cumulative sum is not in the hashmap, add it along with the current node to the hashmap.
7. After traversal, return the next node of the dummy node as the head of the modified linked list.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
- Space complexity: O(n), where n is the number of distinct cumulative sums encountered in the linked list. In the worst case, all cumulative sums are distinct, and the hashmap stores n entries. Additionally, the space complexity of the output linked list is also O(n).

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
