# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #a fast and a slow pointer
        slow = head
        fast = head

        while fast and fast.next :
            #iterate and check to see if they are equal
            #slow += 1
            slow = slow.next
            
            #fast += 2
            fast = fast.next.next

            #now check values
            if slow == fast :
                return True

        #if we are outside the while loop, then we hit a null
        return False 