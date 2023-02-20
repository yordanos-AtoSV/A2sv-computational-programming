# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if m == n :
        return head
    dummy = ListNode(0, next = head)
    prev = dummy
    cur = head 
    for i in range(m -1):
        prev = cur
        cur = cur.next
        
    nex = cur.next
 
    for i in range(n - m ):
  
        temp = nex.next
        nex.next = cur
        cur = nex
        nex = temp
  
    prev.next.next = nex    
    prev.next = cur
  
    

    
    return dummy.next

