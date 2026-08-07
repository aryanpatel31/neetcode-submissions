# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(None)
        prev = dummy

        while l1 or l2 or carry:
            int1 = l1.val if l1 else 0
            int2 = l2.val if l2 else 0
            
            new_node_val = int1 + int2 + carry
            if new_node_val > 9:
                new_node_val = new_node_val % 10
                carry = 1
            else:
                carry = 0
            
            new_node = ListNode(new_node_val)
            prev.next = new_node
            prev = new_node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


    
         

            
