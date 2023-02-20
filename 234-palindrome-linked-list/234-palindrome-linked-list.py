# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        check = []
        while head:
            check.append(head.val)
            head = head.next
    
       
        if check != list(reversed(check)):
            return False
        else:
            return True
      
            
        