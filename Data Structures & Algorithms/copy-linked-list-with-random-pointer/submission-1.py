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
        
        if not head:
            return None
        
        #first pass
        node_map = {}
        head1 = head
        while head1:
            node_map[head1] = Node(head1.val, None, None)
            head1 = head1.next
            
        #second pass
        head2 = node_map[head] 
        if head.next:
            head2.next = node_map[head.next]
        else:
            head2.next = None
        if head.random:
            head2.random = node_map[head.random]
        else:
            head2.random = None

        head = head.next

        while head:
            new_node = node_map[head]
            if head.next:
                new_node.next = node_map[head.next]
            else:
                new_node.next = None
            if head.random:
                new_node.random = node_map[head.random]
            else:
                new_node.random = None
            head = head.next

        return head2


            



        
