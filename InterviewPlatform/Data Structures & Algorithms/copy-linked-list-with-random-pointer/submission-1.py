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

        curr = head
        master_dict = {}
        new_node = Node(curr.val, curr.next, curr.random)
        master_dict[curr] = new_node
        head_new = new_node
        prev = head_new
        curr = curr.next        
        while curr:
            new_node = Node(curr.val, curr.next, curr.random)
            master_dict[curr] = new_node
            prev.next = new_node
            prev = new_node

            curr = curr.next


        curr = head_new
        while curr:
            curr.random = master_dict.get(curr.random, None)
            curr = curr.next


        return head_new



            
        