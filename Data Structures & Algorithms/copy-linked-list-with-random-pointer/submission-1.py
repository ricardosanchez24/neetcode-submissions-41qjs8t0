"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

          copyHash = {None:None}

          curr = head

          while curr:
            copy = Node(curr.val)
            copyHash[curr] = copy
            curr = curr.next

          curr = head

          while curr:
            copy = copyHash[curr]
            copy.next = copyHash[curr.next]
            copy.random = copyHash[curr.random]
            curr = curr.next

          return copyHash[head]       