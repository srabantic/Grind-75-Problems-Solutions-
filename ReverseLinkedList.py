from typing import Optional
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head 
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next 
        return prev

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
print(solution.reverseList(head).val)
