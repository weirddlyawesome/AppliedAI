# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        p_trs = []
        curr = head
        while curr:
            p_trs.append(curr)
            curr = curr.next

        l = 0
        r = len(p_trs) - 1

        while l < r:
            
            p_trs[l].next = p_trs[r]

            if l + 1 < r :
                p_trs[r].next = p_trs[l + 1]

            l += 1
            r -= 1

        p_trs[len(p_trs)//2].next = None







