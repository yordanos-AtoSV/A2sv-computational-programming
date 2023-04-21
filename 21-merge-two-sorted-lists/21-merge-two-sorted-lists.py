# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        cur1 = list1
        cur2 = list2
        if not cur1 and not cur2:
            return 
        while cur1 and cur2 :
            if cur1.val < cur2.val:
                temp.next = ListNode(cur1.val) 
                temp = temp.next
             
                cur1 = cur1.next
 
       
                    
            else:
                temp.next = ListNode(cur2.val) 
                temp = temp.next
            
                cur2 = cur2.next
        
            
        if cur1:
           
                temp.next = cur1
             
        if cur2:
            
                temp.next = cur2
               
            
        return dummy.next
