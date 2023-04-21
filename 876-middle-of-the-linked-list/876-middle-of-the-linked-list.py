# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            
       
        mid = (count // 2) 
        cur = head
        while cur and mid > 0:
            cur = cur.next
            mid -= 1
  
            
        return cur