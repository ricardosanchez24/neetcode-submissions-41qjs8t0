# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      nod = ListNode(0,head)
      two = nod
      one = head

      while n > 0:

        one = one.next
        n -=1

      while one:
        one = one.next
        two = two.next

      two.next = two.next.next

      return nod.next        