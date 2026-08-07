# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        new_head_val = (l1.val + l2.val) % 10

        if (l1.val + l2.val )> 9:
            carry = 1

        new_head = ListNode(new_head_val)
        prev = new_head
        
        l1 = l1.next
        l2 = l2.next
        
        while l1 and l2:

            new_node_val = carry + l1.val + l2.val 
           
            if new_node_val > 9:
                new_node_val = new_node_val % 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(new_node_val)
            prev.next = new_node
            prev = new_node

            l1 = l1.next
            l2 = l2.next

        while l1:
            new_node_val = carry + l1.val

            if new_node_val > 9:
                new_node_val = new_node_val % 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(new_node_val)
            prev.next = new_node
            prev = new_node
            l1 = l1.next
            
        while l2:
            new_node_val = carry + l2.val

            if new_node_val > 9:
                new_node_val = new_node_val % 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(new_node_val)
            prev.next = new_node
            prev = new_node
            l2 = l2.next

        if carry:
            new_node_val = carry
            new_node = ListNode(carry)
            prev.next = new_node
            prev = new_node

        return new_head

    
         

            
