# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [ 1 ] -> [ 2 ] -> [ 3 ]
        # current = None
        # next_val = [ 1 ]
        # temp = None
        #
        # while loop 
        # 1st: next_val = [ 2 ]
        # current = 
        # [ 1 ] <- [ 2 ] -> [ 3 ]
        #
        #
        #
        #
        #
        #
        #
        # [ 1 ] <- [ 2 ] <- [ 3 ]
        current = None
        next_val = head
        temp = None


        while(next_val != None):
            temp =  next_val.next
            next_val.next = current
            current = next_val
            next_val = temp 

        return current