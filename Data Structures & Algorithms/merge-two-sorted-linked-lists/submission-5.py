# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        c1,c2 = list1, list2  
        n = None  

        head = ListNode(n)
        curr = head


        while c1 is not None and c2 is not None:

            if c1.val <= c2.val:
                curr.next = c1
                curr = curr.next  
                c1 = c1.next   
            else:
                curr.next = c2
                curr = curr.next
                c2 = c2.next 
        
        if c1 is None:
            curr.next = c2
        else:
            curr.next = c1    

                    
        return head.next       