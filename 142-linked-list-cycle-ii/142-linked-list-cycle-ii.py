# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head 
        flag = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast :
                flag = True
                break
                
        if flag == True:        
            slow2 = head
            pos = 0
            while slow2 and fast:
                if slow2 == fast:
                    break 
                slow2 = slow2.next
                fast = fast.next
                pos += 1
               
          
            cur = head
            while cur and pos > 0:
                cur = cur.next
                pos -= 1
            return cur
        
     
        return 