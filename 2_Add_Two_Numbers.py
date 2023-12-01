import unittest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

class addTwoNumbersTest(unittest.TestCase):
    def test_addTwoNumbers_case1(self, l1=[2,4,3], l2=[5,6,4], solution=[7,0,8]):
        output = addTwoNumbers(list_to_linked_list(l1), list_to_linked_list(l2))
        self.assertEqual(linked_list_to_list(output), solution)

    def test_addTwoNumbers_case2(self, l1=[0], l2=[0], solution=[0]):
        output = addTwoNumbers(list_to_linked_list(l1), list_to_linked_list(l2))
        self.assertEqual(linked_list_to_list(output), solution)

    def test_addTwoNumbers_case3(self, l1=[9,9,9,9,9,9,9], l2=[9,9,9,9], solution=[8,9,9,9,0,0,0,1]):
        output = addTwoNumbers(list_to_linked_list(l1), list_to_linked_list(l2))
        self.assertEqual(linked_list_to_list(output), solution)

if __name__ == "__main__":
    unittest.main()