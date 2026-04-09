# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

       #1- capturar las dos cabezas 
       #2- iniciar una nueva lista con la cabeza en null
       #3- recorrer ambas lista hasta que se acabe los valores de la lista mas larga
       #4- obtener los valores de los nodos
       #5- manejar el caso de que los nodos sean nulos
       #6- sumar los valores de los nodos y amacenarlos en una variable
       #7- agg el nuevo nodo en la nueva lista
       #8- retornar la cabeza de la nueva lista
       #extra- contar las dos listas para encontrar la lista mas larga
       

       head_1 = l1
       head_2 = l2

       head_new = None

       acarr = 0

       while head_1 or head_2 or acarr:
        suum = 0
        val1 = head_1.val if head_1 else 0
        val2 = head_2.val if head_2 else 0

        suum = val1 + val2 + acarr
        acarr = suum // 10
        va = suum % 10
        node_new = ListNode(va)
        

        if head_new is None:
            head_new = node_new
            current = head_new
        else:
            
            current.next = node_new
            current = current.next

        if head_1: head_1 = head_1.next
        if head_2: head_2 = head_2.next    

       return  head_new
        


