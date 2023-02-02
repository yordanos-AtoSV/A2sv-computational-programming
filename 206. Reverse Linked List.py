# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head :
            return head
        else:
            cur = head
        next = head.next

        while next != None:
            cur.next = prev
            prev = cur 
            cur = next
            next =  next.next
        cur.next = prev
        head = cur

        
        
      
        return head
