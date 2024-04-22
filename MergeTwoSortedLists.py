"""
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
"""
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode()
        current = result_list
        while (list1 and list2):
            if (list1.val < list2.val):
                current.next = list1
                list1 = list1.next 
            else:
                current.next = list2 
                list2 = list2.next 
            current = current.next 
        current.next = list1 or list2 
        return result_list.next
