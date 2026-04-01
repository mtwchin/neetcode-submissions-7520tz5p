# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        outail = out

        #while both list1 head and list2 head exist,

        while list1 and list2:
            if list1.val <= list2.val:
                outail.next = list1
                list1 = list1.next
            else:
                outail.next = list2
                list2 = list2.next
            outail = outail.next
        
        #if list1 still exists (if list1 is longer than list2, just append list1 to the output list)
        if list1:
            outail.next = list1
        elif list2:
            outail.next = list2
        return out.next


