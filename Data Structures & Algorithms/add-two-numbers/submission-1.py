# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #new linked list
        head = ListNode()
        curr = head
        carry = 0

        while l1 or l2 or carry :
            #first check which is null and which isn't 
            if l1 :
                d1 = l1.val
            else :
                d1 = 0
            if l2 :
                d2 = l2.val
            else :
                d2 = 0
            
            #now lets sum it up
            sum = d1 + d2 + carry

            #now supposed the sum was > 9
            carry = sum // 10
            sum = sum % 10
            

            curr.next = ListNode(sum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next