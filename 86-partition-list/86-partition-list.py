# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head 
        less = ListNode(-1)
        lesshead = less
        greater = ListNode(-1)
        greaterhead = greater
        
        while cur:
            if(cur.val < x):
                less.next = cur
                cur = cur.next
                less = less.next
            else:
          
                greater.next = cur
                
                cur = cur.next
                greater = greater.next
                
    
        less.next = greaterhead.next
        greater.next = None 
        print(less)
        
        
        return lesshead.next
            


        
            
            
            
            
        