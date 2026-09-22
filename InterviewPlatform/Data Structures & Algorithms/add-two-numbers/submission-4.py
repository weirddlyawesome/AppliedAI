# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = l1
        list2 = l2
        carry_flag = 0

        new_list_head = self.find_longer(l1, l2)
        new_list = new_list_head

        while list1 and list2:
            sum = list1.val + list2.val + carry_flag
            val = sum % 10
            carry_flag = sum // 10

            new_list.val = val

            list1 = list1.next
            list2 = list2.next
            prev = new_list
            new_list = new_list.next

        if new_list_head == l1:
            if carry_flag == 0:
                return new_list_head
            else:
                while list1:
                    sum = list1.val + carry_flag
                    val = sum % 10
                    carry_flag = sum // 10

                    new_list.val = val

                    list1 = list1.next
                    prev = new_list
                    new_list = new_list.next


        if new_list_head == l2:
            if carry_flag == 0:
                return new_list_head
            else:
                while list2:
                    sum = list2.val + carry_flag
                    val = sum % 10
                    carry_flag = sum // 10

                    new_list.val = val

                    list2 = list2.next
                    prev = new_list
                    new_list = new_list.next


        if carry_flag:
            new_node = ListNode(1, None)
            prev.next = new_node

        return new_list_head


             
    def find_longer(self, l1, l2):
        length1 = 0
        length2 = 0
        head_1 = l1
        head_2 = l2
        while l1:
            length1 += 1
            l1 = l1.next

        while l2:
            length2 += 1
            l2 = l2.next 

        return (head_1 if length1>= length2 else head_2)  