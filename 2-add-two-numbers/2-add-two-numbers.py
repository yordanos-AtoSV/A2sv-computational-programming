# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        cur1 = l1
        cur2 = l2
        
        while cur1 :
           
            num1.append(cur1.val) 
                
            if cur1.next:
                cur1 = cur1.next
            else:
                break
                
        while cur2:
           
            num2.append(cur2.val)
                     
            if cur2.next:
                cur2 = cur2.next 
            else:
                break
                
        num1.reverse()
        num2.reverse()
        num1 = "".join(map(str, num1))
        num2 = "".join(map(str, num2))
        sums = int(num1) + int(num2) 
        sums = list(str(sums))
        sums.reverse()
        head = ListNode(sums[0])
        cur = head
        for num in sums[1:]:
           
            temp = ListNode(num)
            cur.next = temp
            cur = temp
            

        return head