# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #linked list to store the sum
        head = ListNode()
        curr = head
        carry = 0

        while l1 or l2 or carry:
            #get the digits of each list
            #if null its just going to be 0
            if l1 :
                d1 = l1.val
            else :
                d1 = 0
            if l2 :
                d2 = l2.val
            else :
                d2 = 0
            
            #sum it up and use the carry if need be
            sum = d1 + d2 + carry

            #extract the new carry
            carry = sum // 10

            #get only the ones place of the sum
            sum = sum % 10

            curr.next = ListNode(sum)

            #update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
