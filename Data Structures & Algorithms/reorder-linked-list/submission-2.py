# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        init = head
        s = head
        f = head
        
        while f != None and f.next != None:
            
            s = s.next
            f = f.next.next
        
        prev = None
        curr = s.next
        s.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while init != None and prev != None:
            nxt_init = init.next
            nxt_prev = prev.next

            init.next = prev
            prev.next = nxt_init

            init = nxt_init
            prev = nxt_prev

        return prev