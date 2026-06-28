# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # iniciar una tortuga y una liebre
        fast = head
        low = head
        # recorrer la lista con la tortuga y la liebre hasta que la liebre llegue al final
        while fast and fast.next:
            # hacer avanzar la tortuga un paso y a la liebre dos
            fast = fast.next.next
            low = low.next
            # verificar si la liebre encuentra a la tortuga
            if fast == low:
                # si es asi retorna verdadero
                return True
                # si no seguir

        # si despues de recorrer la lista no se encontraron retornar false 
        return False   