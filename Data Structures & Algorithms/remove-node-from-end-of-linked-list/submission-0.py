# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 1
        
        s = head
        while s.next:
            length += 1
            s = s.next
        
        index = (length - n)
        
        if index == 0:
            cur = head
            head = head.next
            cur.next = None
            return head


        prev = None
        curr = head

        for _ in range(index):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr.next = None

        return head