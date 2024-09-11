"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

IMPLEMENTATION: Space Complexity - O(1)
Floyd's cycle-finding algorithm is a pointer algorithm that uses only two pointers, which move through the sequence at different speeds. 
It is also called the "tortoise and the hare algorithm", alluding to Aesop's fable of The Tortoise and the Hare.
It is used to find a loop/cycle in a linked list.
In this algorithm, if there is a cycle then it is almost gurenteed that slow and fast at some point will 
point to the same node.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False
        
        slow_pointer = fast_pointer = head

        while (fast_pointer.next and fast_pointer.next.next) is not None:

            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        
        return False

solution = Solution()
head = ListNode(3)
l1 = ListNode(2)
l2 = ListNode(0)
l3 = ListNode(-4)

head.next = l1
l1.next = l2
l2.next = l3
l3.next = l1

print(solution.hasCycle(head))

head1 = ListNode(1)
print(solution.hasCycle(head1))


            
