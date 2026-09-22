# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.len_utility(head)
        if length == 1:
            return None
        pos_front = length - n
       
        if pos_front == 0:
            return head.next

        curr = head

        for i in range(pos_front-1):
            curr = curr.next

        curr.next = curr.next.next
        
        return head




    def len_utility(self, head):
        res = 0
        curr= head

        while curr:
            res += 1
            curr = curr.next

        return res
            
        