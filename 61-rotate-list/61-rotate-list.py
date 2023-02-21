# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or (head and head.next == None):
            return head
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
            
        k = k %  count  
        for i in range(k ):
         
            prev = None
            ptr = head
            while ptr.next != None:
                prev = ptr
                ptr = ptr.next
                
            ptr.next = head
            prev.next = None
            head = ptr
            
           
        
       
        return head
        