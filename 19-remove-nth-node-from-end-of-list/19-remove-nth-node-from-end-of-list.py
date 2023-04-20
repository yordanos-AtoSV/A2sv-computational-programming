# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur :
            size += 1
            if cur.next:
                cur = cur.next
            else:
                break
        
        print(size)
        if size == 1:
            return 
        
        n = (size)- n   
        if n > 0:
            n -= 1
            cur = head
            while cur and n > 0:
                cur = cur.next
                n -= 1

            if cur and n == 0 and cur.next :

                cur.next = cur.next.next

        else:
            head = head.next
                
        return head