from typing import Optional
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, first = head, head

        while first and first.next:
            slow = slow.next
            first = first.next.next
        return slow

head = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)

head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

solution = Solution()
print(solution.middleNode(head).val)

head1 = ListNode(1)
l5 = ListNode(2)
l6 = ListNode(3)
l7 = ListNode(4)
l8 = ListNode(5)
l9 = ListNode(6)

head1.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9

print(solution.middleNode(head1).val)