# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        arr = []
        v = None

        if list1 is None:
            return list2
        elif list2 is None:
            return list1    

        while c1 is not v:  
            arr.append(c1.val)
            c1 = c1.next
            
        while c2 is not v:
            arr.append(c2.val)
            c2 = c2.next

        arr.sort()


        head = ListNode(arr[0])
        current = head
        
        # Iterar sobre el resto del array y crear nodos
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
            
        return head
            