# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #compare the heads and keep adding the smaller value to the new list
        curr = ListNode()
        #head pointer to keep track of head node for returning
        head = curr
        #now iterate through the two lists
        while list1 and list2 :
            #check which list head is smaller
            if list1.val < list2.val :
                #add list one to the new list
                curr.next = list1
                #move list1 to the next node
                list1 = list1.next
            else :
                #list2 is greater or they are equal
                curr.next = list2
                #iterate list2 up
                list2 = list2.next
            curr = curr.next
        #then add what ever list isn't null
        if list1 :
            curr.next = list1
        elif list2 :
            curr.next = list2
        return head.next