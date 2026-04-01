# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev





        #prev = head
        #cur = prev

        #while head.next:
        #    cur = head.next
        #    cur.next = prev
        #    prev = cur
        #    head = head.next

        #return cur

        


            
