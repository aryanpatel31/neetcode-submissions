# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 3 steps
            # 1. find middle
            # 2. reverse second list
            # 3. merge

        
        #find middle

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        #reversing second
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        
        #merging
        second = prev
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


                



        
        
        
                

            