# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        monostack = []
        arr = []
        ans = [0] * count
        cur = head 
        i = 0 
        while cur:
            while monostack and arr[monostack[-1]] < cur.val:
                temp  = monostack.pop()
                ans[temp] = cur.val
                
            monostack.append(i)
            arr.append(cur.val)
            i += 1
            cur = cur.next
            
            
        return ans