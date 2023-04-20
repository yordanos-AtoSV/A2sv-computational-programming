# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
                if cur.next:
                    if cur.val == cur.next.val:
                        cur.next = cur.next.next
                        while cur.next and cur.val == cur.next.val:
                            cur.next = cur.next.next
                          
                    cur = cur.next
                else:
                    break
        return head
                
        