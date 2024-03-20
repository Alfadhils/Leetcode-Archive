class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = 0
        current = list1
        while (current != None and start < a - 1):
            current = current.next
            start +=1
        remove = current.next
        current.next = list2
        end = start
        while (remove != None and end < b):
            remove = remove.next
            end +=1
        while (list2.next != None):
            list2 = list2.next
        list2.next = remove
        return list1