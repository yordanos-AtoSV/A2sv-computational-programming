# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        oddH = head
        evenH = head.next
        oddp = oddH
        evenp = evenH
        
        while evenp != None:
            if evenp.next != None:
                oddp.next = evenp.next
            else:
                oddp.next = evenH
                return oddH
            
            oddp = oddp.next
            evenp.next = oddp.next
            evenp = evenp.next
            
        oddp.next = evenH
        return oddH
            
        
        