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

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    length = 0
    curr = head
    while curr is not None:
        curr = curr.next
        length += 1
    
    for i in range(int(length/2)):
        head = head.next
    return head

class middleNodeTest(unittest.TestCase):
    def test_middleNode_case1(self, head=[1,2,3,4,5], solution=[3,4,5]):
        output = middleNode(list_to_linked_list(head))
        self.assertEqual(linked_list_to_list(output), solution)

    def test_middleNode_case2(self, head=[1,2,3,4,5,6], solution=[4,5,6]):
        output = middleNode(list_to_linked_list(head))
        self.assertEqual(linked_list_to_list(output), solution)

    def test_middleNode_case3(self, head=[1,1,2,2,3,3,4,4], solution=[3,3,4,4]):
        output = middleNode(list_to_linked_list(head))
        self.assertEqual(linked_list_to_list(output), solution)

if __name__ == "__main__":
    unittest.main()