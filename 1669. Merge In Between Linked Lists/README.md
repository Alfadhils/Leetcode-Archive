# 1669. Merge In Between Linked Lists

## Intuition
To merge two linked lists between given indices `a` and `b`, we can traverse through the first list until we reach index `a - 1`, then we keep track of the node at index `a`, and continue traversing until index `b`. Then, we connect the end of the first list to the start of the second list, effectively merging the two lists.

## Approach
1. Initialize a pointer `current` to traverse through the first list until index `a - 1`.
2. Keep track of the node at index `a`.
3. Traverse from index `a` to index `b` and keep track of the node at index `b`.
4. Connect the end of the first list to the start of the second list.
5. Traverse through the second list to reach its end.
6. Connect the end of the second list to the node after index `b` in the first list.
7. Return the head of the first list.

## Complexity
- Time complexity: O(n), where n is the total number of nodes in the first list.
- Space complexity: O(1).

## Code
```python
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = 0
        current = list1

        while current is not None and start < a - 1:
            current = current.next
            start += 1

        remove = current.next
        current.next = list2
        end = start

        while remove is not None and end < b:
            remove = remove.next
            end += 1

        while list2.next is not None:
            list2 = list2.next

        list2.next = remove
        return list1
```