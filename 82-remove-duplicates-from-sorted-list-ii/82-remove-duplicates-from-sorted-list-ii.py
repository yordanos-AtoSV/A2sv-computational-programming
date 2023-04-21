# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head
            
            thenext = head.next
            
            if head.val == thenext.val:
                while thenext and head.val == thenext.val :
                    thenext = thenext.next
                return self.deleteDuplicates(thenext)
            
            else:
                head.next = self.deleteDuplicates(thenext)
                return head