# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head 
        check = []
        while cur:
            check.append(cur.val)
            cur = cur.next
        temp = list(reversed(check))
       
        if check != temp:
            return False
        else:
            return True
      
            
        